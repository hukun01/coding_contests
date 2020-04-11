rr = input
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

####
def solve(R, C, A):
    UP, DOWN, LEFT, RIGHT, VAL = 0,1,2,3, 4
    competitors = [[None,None,None,None,None, _] for _ in range(R*C)]
    for r, row in enumerate(A):
        for c, val in enumerate(row):
            competitors[r*C + c][VAL] = val
    for r in range(R-1):
        for c in range(C):
            competitors[r*C + c][DOWN] = competitors[r*C + C + c]
            competitors[r*C + C + c][UP] = competitors[r*C + c]
    for r in range(R):
        for c in range(C-1):
            competitors[r*C + c][RIGHT] = competitors[r*C + c + 1]
            competitors[r*C + c + 1][LEFT] = competitors[r*C + c]

    
    s = sum(sum(row) for row in A)
    ans = 0
    while competitors:
        ans += s
        kill = set()
        for i, node in enumerate(competitors):
            neitot = 0
            neisum = 0
            for d in range(4):
                chi = node[d]
                if chi is not None:
                    neisum += chi[VAL]
                    neitot += 1
            if neitot and neisum > node[VAL] * neitot:
                kill.add(i)
        if not kill: break
        competitors2 = []
        seen = {competitors[i][-1] for i in kill}
        for i, node in enumerate(competitors):
            if i in kill:
                s -= node[VAL]
                for d in range(4):
                    chi = node[d]
                    past = node[d^1]
                    if past:
                        if past[d]:
                            past[d] = chi
                    if chi:
                        if chi[d^1]:
                            chi[d^1] = past
                        if chi[-1] not in seen:
                            seen.add(chi[-1])
                            competitors2.append(chi)
        competitors = competitors2
        
    return ans

####

for tc in range(1, 1 + rri()):
    R, C = rrm()
    A = [rrm() for _ in range(R)]
    ans = solve(R, C, A)
    print("Case #{}: {}".format(tc, ans))
