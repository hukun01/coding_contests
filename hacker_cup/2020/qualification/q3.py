from collections import defaultdict

rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(heights):
    '''
    DP.
    An interval can only be formed by merging two intervals i1, i2, when
    i1.right == i2.left.
    Let max_lens[p] be the max max_len ending at point p.
    We have
    max_lens[p] = max(max_lens[p], max_lens[p-h] + h)
    and 
    max_lens[p+h] = max(max_lens[p+h], max_lens[p] + h)
    Note that we need to update max_lens[p+h] first to avoid
    step over max_lens[p].
    '''
    heights.sort()
    max_lens = defaultdict(int)
    for p, h in heights:
        max_lens[p+h] = max(max_lens[p+h], max_lens[p] + h)
        max_lens[p] = max(max_lens[p], max_lens[p-h] + h)
    return max(max_lens.values())

for i in range(1, rri() + 1):
    heights = [list(rrm()) for _ in range(rri())]
    print("Case #{}: {}".format(i, solve(heights)))