
def find(ans, cur, runningSum, n, k):
    if len(cur) == n:
        if runningSum == k:
            ans.extend(cur)
            return True
        else:
            return False
    if runningSum >= k:
        return False
    if runningSum + (n - len(cur)) * n < k:
        return False
    for i in range(1, n + 1):
        cur.append(i)
        if find(ans, cur, runningSum + i, n, k):
            return True
        cur.pop()
    return False

def solve(n, k):
    m = [[set(range(1, n + 1)) for r in range(n)] for c in range(n)]

    ans = []
    find(ans, [], 0, n, k)
    print("found trace for k: ", ans)
    def mark(r, c, val):
        if val not in m[r][c]:
            return False
        for r1 in range(n):
            if val in m[r1][c]:
                m[r1][c].remove(val)
        for c1 in range(n):
            if val in m[r][c1]:
                m[r][c1].remove(val)
        return True

    for r in range(n):
        for c in range(n):
            if r == c:
                if not mark(r, c, ans[r]):
                    return "IMPOSSIBLE"
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if r == c:
                result[r][c] = ans[r]
                continue
            if not m[r][c]:
                return "IMPOSSIBLE"
            for val in list(m[r][c]):
                result[r][c] = val
                if not mark(r, c, val):
                    return "IMPOSSIBLE"
                
    return "POSSIBLE\n"+'\n'.join([' '.join([str(c) for c in row]) for row in result])

def solve2(n, k):
    mask = (1 << n) - 1
    m = [[mask] * n for _ in range(n)]
    # pick n numbers from [1, n], what combos can form k? Duplicates allowed.
    # for each combo, the less different numbers it uses, the more possible
    # we can get a final matrix.
    ans = []
    find(ans, [], 0, n, k)

    def mark(r, c, idx):
        b = bin(m[r][c])[2:].zfill(n)
        #print("r, c, idx, b:", r, c, idx, b)
        if b[idx] == '0':
            return False
        m[r][c] = int(b[:idx] + '0' + b[idx + 1:], 2)
        # mark all cells in the row and col
        for r1 in range(n):
            if r == r1:
                continue
            b = bin(m[r1][c])[2:].zfill(n)
            if b[idx] == '1':
                m[r1][c] = int(b[:idx] + '0' + b[idx + 1:], 2)

        for c1 in range(n):
            if c == c1:
                continue
            b = bin(m[r][c1])[2:].zfill(n)
            if b[idx] == '1':
                m[r][c1] = int(b[:idx] + '0' + b[idx + 1:], 2)
        return True

    for r in range(n):
        for c in range(n):
            if r == c:
                idx = n - ans[r]
                if not mark(r, c, idx):
                    return "IMPOSSIBLE"
    #print("mid-processed: ", m)
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if r == c:
                result[r][c] = ans[r]
                continue
            b = bin(m[r][c])[2:].zfill(n)
            #print("r, c, b: ", r, c, b)
            found = False
            for i in range(len(b)):
                if b[i] == '1':
                    found = True
                    result[r][c] = n - i
                    if not mark(r, c, i):
                        #print("result: ", result)
                        return "IMPOSSIBLE"
                    break
            if not found:
                return "IMPOSSIBLE"
    #if not isGood(n, result):
    #    print("result is not good!!")
    return "POSSIBLE\n"+'\n'.join([' '.join([str(c) for c in row]) for row in result])

def isGood(n, m):
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
    return len(rows) == len(cols) == 0

t = 1
for n in range(2, 6):
    for k in range(n, n ** 2 + 1):
        print("Case #{}: n: {}, k: {}".format(t, n, k))
        result = solve(n, k)
        if result == "IMPOSSIBLE":
            t += 1
            continue
        print("Case #{}: {}".format(t, result))
        t += 1