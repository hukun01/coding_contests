def getInput():
    matrix = []
    N = int(input())
    for _ in range(N):
        matrix.append([int(c) for c in input().split(" ")])
    return (N, matrix)

def solve(n, m):
    seenCols = set()
    seenRows = set()
    cols = set()
    rows = set()
    k = 0
    for r in range(n):
        for c in range(n):
            v = m[r][c]
            if r == c:
                k += v
            if (c, v) in seenCols:
                cols.add(c)
            elif c not in cols:
                seenCols.add((c, v))
            if (r, v) in seenRows:
                rows.add(r)
            elif r not in rows:
                seenRows.add((r, v))
    return (k, len(rows), len(cols))

t = int(input())
for i in range(1, t + 1):
    N, M = getInput()
    print("Case #{}: {} {} {}".format(i, *solve(N, M)))