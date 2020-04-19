rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(n, b):
    A = list(rrm())
    count = 0
    for a in sorted(A):
        if b < a:
            break
        b -= a
        count += 1
    return count

for i in range(1, rri() + 1):
    n, b = rrm()
    print("Case #{}: {}".format(i, solve(n, b)))