rr = input
rri = lambda: int(rr())

'''
In Pascal triangle, the r-th (base 1) row sums up to 2^(r-1).
Given a total N, look at its binary form, from the least
significant bit:
1. if the x-th bit is 1, we need to grab all cells from x-th row in the triangle;
2. otherwise, we need to skip the x-th row.
But to form a consecutive path, we can't completely skip a row. Instead, we can

'''
def solve(n):
    def output(a, b):
        print("{} {}".format(a, b))

    rows = min(30, n)
    n -= rows
    a = [0] * rows
    for r in range(rows-1, -1, -1):
        if n >= (1 << r) - 1:
            a[r] = 1
            n -= (1 << r) - 1
    rows += n
    for _ in range(rows - len(a)):
        a.append(0)
    side = 0
    for r in range(rows):
        if a[r] == 1:
            if side == 0:
                for j in range(r + 1):
                    output(r + 1, j + 1)
            else:
                for j in range(r, -1, -1):
                    output(r + 1, j + 1)
            side ^= 1
        else:
            if side == 0:
                output(r + 1, 1)
            else:
                output(r + 1, r + 1)

t = int(input())
for i in range(1, t + 1):
    print("Case #{}:".format(i))
    solve(rri())