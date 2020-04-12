rr = input
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

'''
Use `python3.7 -m cProfile ./q3.py < q3_input2.txt` to see what's taking the most time.

The key in this problem is to only check for neighbor updates for the persons that are being
eliminated in the last round. Such that there are at most 4 updates to do for each person,
and there is at most R*C persons to eliminate, so the total time can be O(R*C).

Some implementation details are also critical to pass the test set 2 or to make logic concise,
such as:
1. avoid collections.defaultdict(), it's slower than dict() or list().
2. use list comprehension as much as possible.
3. when dealing with directions, let 0 be up, 1 be down, then d^1 is the opposite direction of d,
same applies to left(3) and right(4).
'''
def solve(R, C, A):
    neighbors = [[[(-1, -1)] * 4 for c in range(C)] for r in range(R)]
    # UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def check(r, c):
        return 0 <= r < R and 0 <= c < C

    for r in range(0, R, 2):
        for c in range(0, C, 2):
            for d, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if check(nr, nc):
                    neighbors[r][c][d] = (nr, nc)
                    neighbors[nr][nc][d^1] = (r, c)

    def shouldEliminate(r, c):
        total = 0
        count = 0
        for nr, nc in neighbors[r][c]:
            if nr != -1:
                total += A[nr][nc]
                count += 1
        if count == 0:
            return False
        return (total / count) > A[r][c]

    def updateNeighbors(eliminated):
        toCheck = set()
        for r, c in eliminated:
            neis = neighbors[r][c]
            for d, (nr, nc) in enumerate(neis):
                if nr == -1:
                    continue
                neighbors[nr][nc][d^1] = neis[d^1]
                if (nr, nc) not in eliminated:
                    toCheck.add((nr, nc))

        return set((r, c) for r, c in toCheck if shouldEliminate(r, c))

    intLevel = 0
    currInt = 0
    eliminated = set()
    for r in range(R):
        for c in range(C):
            currInt += A[r][c]
            if shouldEliminate(r, c):
                eliminated.add((r, c))
    intLevel += currInt
    while eliminated:
        goneInt = sum(A[r][c] for r, c in eliminated)
        currInt -= goneInt
        intLevel += currInt
        eliminated = updateNeighbors(eliminated)
    return intLevel

for i in range(1, rri() + 1):
    R, C = rrm()
    A = [rrm() for _ in range(R)]
    ans = solve(R, C, A)
    print("Case #{}: {}".format(i, ans))