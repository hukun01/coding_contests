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
def output(a, b):
    print("{} {}".format(a, b))

def solve(n):
    edges = 30
    if n <= edges:
        for i in range(n):
            output(i + 1, 1)
        return
    n -= edges
    atRight = True
    i = 0
    while edges:
        if (n >> i) & 1:
            if atRight:
                for j in range(i + 1, 0, -1):
                    output(i + 1, j)
            else:
                for j in range(1, i+2):
                    output(i + 1, j)
            atRight = not atRight
        else:
            edges -= 1
            if atRight:
                output(i + 1, i + 1)
            else:
                output(i + 1, 1)
        i += 1

t = int(input())
for i in range(1, t + 1):
    print("Case #{}:".format(i))
    solve(rri())