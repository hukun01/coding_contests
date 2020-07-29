from collections import Counter

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(stones):
    count = Counter(stones)
    return 'Y' if abs(count['A'] - count['B']) == 1 else 'N'

for i in range(1, rri() + 1):
    N = rri()
    stones = rr()
    print("Case #{}: {}".format(i, solve(stones)))