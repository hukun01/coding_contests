from collections import deque
from functools import lru_cache

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

MOD = 10 ** 9 + 7

def solve(N, K, W, L, A1, B1, C1, D1, H, A2, B2, C2, D2):
    #print(f"L {L}, H {H}, W {W}")
    # i starts from 0
    @lru_cache(maxsize=500)
    def get_L(i):
        if i <= K-1:
            return L[i]
        return (A1 * get_L(i-2) + B1 * get_L(i-1) + C1) % D1 + 1
    @lru_cache(maxsize=500)
    def get_H(i):
        if i <= K-1:
            return H[i]
        return (A2 * get_H(i-2) + B2 * get_H(i-1) + C2) % D2 + 1

    last_P = None
    ans = 1
    heights = deque()
    for i in range(N):
        h = get_H(i)
        l = get_L(i)
        #print(f"i {i} h {h} l {l}")
        if i == 0:
            curr_P = h * 2 + W * 2
        else:
            while heights and heights[0][1] < l:
                heights.popleft()
            curr_P = last_P
            w_delta = l - get_L(i-1) - W
            #print(f"w_delta {w_delta}")
            if w_delta <= 0:
                cur_max_h = max([x[0] for x in heights if x[1] >= l], default=h)
                #print(f"adding w {2 * (l - get_L(i-1))}")
                curr_P += 2 * (l - get_L(i-1))
                
                if h > cur_max_h:
                    #print(f"adding h {2 * (h - cur_max_h)}")
                    curr_P += 2 * (h - cur_max_h)
                    cur_max_h = h
            else:
                curr_P += 2 * h + W * 2
        heights.append((h, l + W))
        ans = ans * curr_P % MOD
        last_P = curr_P
        
    return ans

for i in range(1, rri() + 1):
    N, K, W = rrm()
    L = list(rrm())
    A1, B1, C1, D1 = rrm()
    H = list(rrm())
    A2, B2, C2, D2 = rrm()
    print("Case #{}: {}".format(i, solve(N, K, W, L, A1, B1, C1, D1, H, A2, B2, C2, D2)))