from functools import lru_cache
from sortedcontainers import SortedList

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

MOD = 10 ** 9 + 7

def solve(N, K, W, L, Al, Bl, Cl, Dl, H, Aw, Bw, Cw, Dw, Ah, Bh, Ch, Dh):
    # i starts from 0
    @lru_cache(maxsize=5)
    def get_L(i):
        if i <= K-1:
            return L[i]
        return (Al * get_L(i-2) + Bl * get_L(i-1) + Cl) % Dl + 1
    @lru_cache(maxsize=5)
    def get_W(i):
        if i <= K-1:
            return W[i]
        return (Aw * get_W(i-2) + Bw * get_W(i-1) + Cw) % Dw + 1
    @lru_cache(maxsize=5)
    def get_H(i):
        if i <= K-1:
            return H[i]
        return (Ah * get_H(i-2) + Bh * get_H(i-1) + Ch) % Dh + 1

    ans = 1
    used_ws = SortedList()
    last_P = 0
    DEBUG = 0
    for i in range(N):
        h = get_H(i)
        l = get_L(i)
        w = get_W(i)
        if DEBUG: print(f"i {i} h {h} l {l} w{w}")
        intersected = 0
        interval = [l, l + w]
        curr_P = last_P
        if used_ws:
            left = used_ws.bisect_right([interval[0]])
            if left > 0 and used_ws[left-1][1] >= interval[0]:
                left -= 1
            right = left
            while right < len(used_ws) and used_ws[right][0] <= interval[1]:
                if right > left:
                    curr_P += 2 * (used_ws[right][0] - used_ws[right-1][1])
                right += 1
            if DEBUG: print(f"left {left}, right {right}")
            intersected = right - left
        if intersected:
            #if DEBUG: print(f"middle {middle}")
            #if DEBUG: print(f"minus h {2 * (intersected - 1) * h}")
            #if DEBUG: print(f"add left side {max(0, used_ws[left][0] - interval[0]) * 2}")
            #if DEBUG: print(f"add right side {max(0, interval[1] - used_ws[right-1][1]) * 2}")
            curr_P += max(0, used_ws[left][0] - interval[0]) * 2
            curr_P += max(0, interval[1] - used_ws[right-1][1]) * 2
            curr_P -= 2 * (intersected - 1) * h
            merged = [min(used_ws[left][0], interval[0]), max(used_ws[right-1][1], interval[1])]
            del used_ws[left:right]
            used_ws.add(merged)
        else:
            curr_P += w * 2 + h * 2
            used_ws.add(interval)
        #if DEBUG: print(f"intersected {intersected}")
        if DEBUG: print(f"used_ws {used_ws}")
        #if DEBUG: print(f"curr_P {curr_P}")
        ans = ans * curr_P % MOD
        last_P = curr_P % MOD
        
    return ans

for i in range(1, rri() + 1):
    N, K = rrm()
    L = list(rrm())
    Al, Bl, Cl, Dl = rrm()
    W = list(rrm())
    Aw, Bw, Cw, Dw = rrm()
    H = list(rrm())
    Ah, Bh, Ch, Dh = rrm()
    print("Case #{}: {}".format(i, solve(N, K, W, L, Al, Bl, Cl, Dl, H, Aw, Bw, Cw, Dw, Ah, Bh, Ch, Dh)))