import os

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(N):
    I = rr()
    O = rr()
    ans = [['N'] * N for _ in range(N)]
    for i in range(N - 1):
        ans[i][i] = 'Y'
        j = i + 1
        ans[j][j] = 'Y'
        if O[i] == 'Y' and I[j] == 'Y':
            ans[i][j] = 'Y'
        if O[j] == 'Y' and I[i] == 'Y':
            ans[j][i] = 'Y'

    for r in range(N):
        for c in range(N):
            if ans[r][c] == 'Y' or O[r] == 'N' or I[c] == 'N':
                continue
            for k in range(N):
                if ans[r][k] == ans[k][c] == 'Y':
                    ans[r][c] = 'Y'

    return os.linesep + os.linesep.join([''.join(c for c in row) for row in ans])

for i in range(1, rri() + 1):
    N = rri()
    print("Case #{}: {}".format(i, solve(N)))