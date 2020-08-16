from collections import deque
from functools import lru_cache

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

MOD = 10 ** 9 + 7

def solve(N, K, W, L, Al, Bl, Cl, Dl, H, Ah, Bh, Ch, Dh):
    # i starts from 0
    @lru_cache(maxsize=500)
    def get_L(i):
        if i <= K-1:
            return L[i]
        return (Al * get_L(i-2) + Bl * get_L(i-1) + Cl) % Dl + 1
    @lru_cache(maxsize=500)
    def get_H(i):
        if i <= K-1:
            return H[i]
        return (Ah * get_H(i-2) + Bh * get_H(i-1) + Ch) % Dh + 1

    last_P = None
    ans = 1
    heights = deque()
    for i in range(N):
        h = get_H(i)
        l = get_L(i)
        if i == 0:
            curr_P = h * 2 + W * 2
        else:
            while heights and heights[0][1] < l:
                heights.popleft()
            curr_P = last_P
            w_delta = l - get_L(i-1) - W
            if w_delta <= 0:
                cur_max_h = max([x[0] for x in heights if x[1] >= l], default=h)
                curr_P += 2 * (l - get_L(i-1))
                
                if h > cur_max_h:
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
    Al, Bl, Cl, Dl = rrm()
    H = list(rrm())
    Ah, Bh, Ch, Dh = rrm()
    print("Case #{}: {}".format(i, solve(N, K, W, L, Al, Bl, Cl, Dl, H, Ah, Bh, Ch, Dh)))