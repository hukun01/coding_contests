rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(n, d):
    A = list(rrm())
    # the later the better for each a in A
    while d > 0 and len(A) > 0:
        a = A.pop()
        while d and d % a != 0:
            d -= d % a
    return d

for i in range(1, rri() + 1):
    n, d = rrm()
    print("Case #{}: {}".format(i, solve(n, d)))