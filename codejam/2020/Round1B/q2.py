rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(x, y):
    return ""

t, a, b = rrm()
for i in range(1, t + 1):
    x, y = rrm()
    print("Case #{}: {}".format(i, solve(x, y)))