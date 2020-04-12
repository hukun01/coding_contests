rr = input
rri = lambda: int(rr())

'''
In Pascal triangle, the r-th (base 1) row sums up to 2^(r-1).
Given N, look at its binary form, from the least significant bit:
1. if the x-th bit is 1, we need to grab the whole x-th row in the triangle;
2. otherwise, we need to skip the x-th row.
But to form a consecutive path, we can't completely skip a row.

We know that because N <= 10^9, and 10^9 < 2^30, so in total we would
use less than 30 rows.

To get closer to the answer, we can go down one side of the triangle with 1s,
if we see 0 at the least significant bits.
And when we see 1, we take the whole row, and go to the other side of the triangle.
We will have to take extra 1s when seeing 0 at the bits, so we can first try to
construct N - 30, and keep going down one side of the triangle afterwards to collect
the rest using 1s.
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