rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(n, k, p):
    stacks = [list(rrm()) for _ in range(n)]
    def dfs(sIdx, pIdx, remain):
        if remain == 0:
            return 0
        if sIdx == len(stacks) or pIdx == len(stacks[sIdx]):
            return 0
        res = 0
        for s in range(sIdx, len(stacks)):
            for p in range(pIdx, len(stacks[s])):
                res = max(res, stacks[s][p] + dfs(s, p + 1, remain - 1), dfs(s + 1, 0, remain))
        return res

    return dfs(0, 0, p)

for i in range(1, rri() + 1):
    n, k, p = rrm()
    print("Case #{}: {}".format(i, solve(n, k, p)))