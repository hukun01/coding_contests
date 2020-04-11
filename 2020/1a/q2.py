def getInput():
    k = int(input())
    return k

def solve(k):
    return 0

t = int(input())
for i in range(1, t + 1):
    k = getInput()
    print("Case #{}: {}".format(i, solve(k)))