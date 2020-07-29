from collections import deque
from math import inf

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

class MinQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def push(self, x, pos):
        while self.queue and self.queue[-1][0] > x:
            self.queue.pop()
        self.queue.append([x, pos])

    def pop_expired(self, pos):
        if self.queue and pos - self.queue[0][1] > self.size:
            self.queue.popleft()

    def min(self):
        return self.queue[0][0]

def solve(n, m, costs):
    '''
    More explanation in
    https://www.facebook.com/codingcompetitions/hacker-cup/2020/qualification-round/problems/D1

    Let F_i be the min cost to arrive at city i with full tank.
    Let G_i be the min cost to arrive at city i.
    Then we have below:
    F_i = G_i = 0
    G_i = min(F_j for j in [i - m, i))
    F_i = G_i + C_i

    Use a queue that maintains all the relevant F_i in the
    sliding window [i - m, i].
    '''
    f_i = MinQueue(m)
    f_i.push(0, 0)
    for i in range(1, n):
        f_i.pop_expired(i)

        c = costs[i] if costs[i] > 0 else inf
        f_i.push(f_i.min() + c, i)

    return f_i.min() if f_i.min() < inf else -1

for i in range(1, rri() + 1):
    N, M = rrm()
    costs = [rri() for _ in range(N)]
    print("Case #{}: {}".format(i, solve(N, M, costs)))