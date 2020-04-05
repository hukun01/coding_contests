import random

def getInput():
    return [int(c) for c in input().split(" ")]

def find(used, candidate, cur, runningSum, n, k):
    if len(cur) == n:
        candidate.clear()
        if runningSum == k:
            ans = list(cur)
            candidate.append(tuple(sorted(ans)))
            if candidate[-1] not in used:
                used.add(candidate[-1])
                return True
        return False
    if runningSum >= k:
        return False
    if runningSum + (n - len(cur)) * n < k:
        return False
    #data = list(range(1, n + 1))
    #random.shuffle(data)
    for i in range(1, n + 1):
        cur.append(i)
        if find(used, candidate, cur, runningSum + i, n, k):
            return True
        cur.pop()
    return False

def fillRest(m, positions, digits, cols, rows):
    if not positions:
        return True
    #print("#pos: ", len(positions))
    x = y = minfree = choices = len(m) + 1
    for r, c in positions:
        row, col = rows[r], cols[c]
        free = row & col
        if len(free) < minfree:
            if len(free) == 0:
                return False
            x, y = c, r
            xrow = row
            xcol = col
            choices = free
            minfree = len(free)

    positions.discard((y, x))
    for choice in choices:
        m[y][x] = choice
        xcol.discard(choice)
        xrow.discard(choice)
        if fillRest(m, positions, digits, cols, rows):
            return True
        xcol.add(choice)
        xrow.add(choice)
    positions.add((y, x))
    
    return False

def fill(m, trace, digits, cols, rows):
    n = len(m)
    positions = set()
    for r in range(n):
        for c in range(n):
            if r == c:
                val = trace[r]
                m[r][c] = val
                rows[r].discard(val)
                cols[c].discard(val)
            else:
                positions.add((r, c))
    #print("prefilled: ", m)
    #print("positions: ", positions)
    return fillRest(m, positions, digits, cols, rows)

def solve(n, k):
    digits = set(range(1, n + 1))
    cols = [{*digits} for _ in range(n)]
    rows = [{*digits} for _ in range(n)]
    used = set()
    candidate = []
    while find(used, candidate, [], 0, n, k):
        print("\nfound traces for k: ", candidate)
        if not candidate:
            break
        m = [[0] * n for _ in range(n)]
        if fill(m, candidate[0], digits, cols, rows):
            return "POSSIBLE\n"+'\n'.join([' '.join([str(c) for c in row]) for row in m])
    return "IMPOSSIBLE"

t = int(input())
for i in range(1, t + 1):
    N, K = getInput()
    #print("N, K: ", N, K)
    print("Case #{}: {}".format(i, solve(N, K)))