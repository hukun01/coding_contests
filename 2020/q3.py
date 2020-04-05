def getInput():
    lines = []
    N = int(input())
    for _ in range(N):
        lines.append([int(c) for c in input().split(" ")])
    return (N, lines)

def solve(n, lines):
    imp = "IMPOSSIBLE"
    activities = [(s, e, i) for i, (s, e) in enumerate(lines)]
    activities.sort()
    ans = [''] * len(lines)
    cEnd = jEnd = 0
    for s, e, i in activities:
        #print("s, e, i: ", s, e, i)
        if cEnd <= s:
            cEnd = e
            ans[i] = 'C'
            continue
        if jEnd <= s:
            jEnd = e
            ans[i] = 'J'
            continue
        return imp
    return ''.join(ans)

t = int(input())
for i in range(1, t + 1):
    n, lines = getInput()
    print("Case #{}: {}".format(i, solve(n, lines)))