from collections import deque
from functools import lru_cache

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

MOD = 10 ** 9 + 7

def solve(N, M, K, S, P, Q, Ap, Bp, Cp, Dp, Aq, Bq, Cq, Dq):
    # i starts from 0
    @lru_cache(maxsize=5)
    def get_P(i):
        if i <= K-1:
            return P[i]
        return (Ap * get_P(i-2) + Bp * get_P(i-1) + Cp) % Dp + 1
    @lru_cache(maxsize=5)
    def get_Q(i):
        if i <= K-1:
            return Q[i]
        return (Aq * get_Q(i-2) + Bq * get_Q(i-1) + Cq) % Dq + 1

    Ps = sorted(get_P(i) for i in range(N))
    Qs = sorted(get_Q(i) for i in range(M))

    def long_enough(m):
        i = j = 0
        while i < N and j < M:
            if (distance := abs(Ps[i] - Qs[j])) + S <= m:
                j_start = j
                j += 1
                while j < M and min(distance, abs(Ps[i] - Qs[j])) + Qs[j] - Qs[j_start] + S * (j - j_start + 1) <= m:
                    j += 1
            i += 1
        return j >= M

    l, h = 0, S*M + 10**9
    while l < h:
        m = (l + h) // 2
        if not long_enough(m):
            l = m + 1
        else:
            h = m

    return h

for i in range(1, rri() + 1):
    N, M, K, S = rrm()
    P = list(rrm())
    Ap, Bp, Cp, Dp = rrm()
    Q = list(rrm())
    Aq, Bq, Cq, Dq = rrm()
    print("Case #{}: {}".format(i, solve(N, M, K, S, P, Q, Ap, Bp, Cp, Dp, Aq, Bq, Cq, Dq)))