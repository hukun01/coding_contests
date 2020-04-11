rr = input
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

def solve(R, C, A):
    neighbors = [[[(-1, -1)] * 4 for c in range(C)] for r in range(R)]
    # UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def check(r, c):
        return 0 <= r < R and 0 <= c < C

    for r in range(R):
        for c in range(C):
            for i, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if check(nr, nc):
                    neighbors[r][c][i] = (nr, nc)
                    
    #print("neighbors: ", neighbors)
    def findNeighborSkills(r, c):
        skills = []
        for nr, nc in neighbors[r][c]:
            if nr != -1:
                skills.append(A[nr][nc])
        if not skills:
            return -1
        return sum(skills) / len(skills)

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

        newEliminated = set()
        for r, c in toCheck:
            if A[r][c] < findNeighborSkills(r, c):
                newEliminated.add((r, c))
        return newEliminated

    intLevel = 0
    currInt = 0
    eliminated = set()
    for r in range(R):
        for c in range(C):
            currInt += A[r][c]
            if A[r][c] < findNeighborSkills(r, c):
                eliminated.add((r, c))
    intLevel += currInt
    while eliminated:
        goneInt = sum(A[r][c] for r, c in eliminated)
        currInt -= goneInt
        intLevel += currInt
        #print("e: ", eliminated)
        eliminated = updateNeighbors(eliminated)
    return intLevel

for i in range(1, rri() + 1):
    R, C = rrm()
    A = [rrm() for _ in range(R)]
    ans = solve(R, C, A)
    print("Case #{}: {}".format(i, ans))