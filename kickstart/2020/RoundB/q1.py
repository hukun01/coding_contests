import math
rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(n):
    A = [math.inf] + list(rrm()) + [math.inf]
    #print("A: ", A)
    return sum(1 for i in range(1, len(A) - 1) if A[i-1] < A[i] > A[i+1])

for i in range(1, rri() + 1):
    n = rrm()
    print("Case #{}: {}".format(i, solve(n)))