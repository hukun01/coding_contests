#!/usr/bin/env python3
import random
import sys

def getInput():
    return [int(c) for c in input().split(" ")]

def interact(s):
    print(s)
    sys.stdout.flush()
    return input()

def flip(s):
    return [str(1 - int(c)) if c.isdigit() else '' for c in s]

def reverse(s):
    return s[::-1]

def both(s):
    return flip(reverse(s))

def solve(b):
    '''
    First, some terminologies:
    'same': array got no change;
    'reverse': array got reversed;
    'flip': array got complemented;
    'both': array got both reversed and complemented.

    Keep track of all indicies we need to query about.
    Build a (partial) array 'ans' to store all the latest values.
    In every round, we randomly pick half indicies for query, the
    other halves are symmetric. The reason behind this is that these
    value pairs would help us know what have happened in the last
    quantum fluctuation, **deterministically**. See method 'update()'
    for more details on how these pairs are used.
    '''
    ROUND = 10
    MAX_QUERIES_COUNT = 150
    def getRandomIndex(candidates):
        if not candidates:
            return 1
        idx = random.sample(candidates, 1)[0]
        candidates.remove(idx)
        return idx
    sames = [] # the index pairs at which the values are the same
    diffs = [] # the index pairs at which the values are different
    indicies = set(range(1, b // 2 + 1))
    queryCount = 0
    ans = [''] * b
    for limit in range(ROUND, MAX_QUERIES_COUNT, ROUND):
        while queryCount + 2 <= limit and indicies:
            queryCount += 2
            i1 = getRandomIndex(indicies)
            ans[i1-1] = interact(str(i1))
            i2 = b + 1 - i1
            ans[i2-1] = interact(str(i2))
            if ans[i1-1] == ans[i2-1]:
                sames.append((i1, i2))
            else:
                diffs.append((i1, i2))
        if not indicies:
            break

        ans, updateQueryCount = update(ans, diffs, sames)
        if updateQueryCount == 1:
            #i1 = getRandomIndex(indicies)
            #ans[i1-1] = interact(str(i1))
            _ = interact('1')
        queryCount += 2
    return interact(''.join(ans))

def update(ans, diffs, sames):
    '''
    Determine the transformation: any of [same, flip, reverse, both].
    Update 'ans' based on the above operation.
    '''
    if len(diffs) == 0 or len(sames) == 0:
        '''
        Two cases:
        1. If diffs has no pairs, ans has all 0 or all 1. No matter how it changes,
            the relative values are going to be the same.
            In another word, flip and reverse operations have the same effect on the values;
            both and same operations have the same effect on the values.
            In this case, we don't need to know which of the two possibilies happened by.
            checking one to see now it's 1 or 0.
        2. If sames has no pairs, all pairs in ans are opposite. This is similar to #1.
        '''
        i1, _ = random.choice(sames) if sames else random.choice(diffs)
        v1Old = ans[i1-1]
        v1New = interact(str(i1))
        if v1Old != v1New:
            ans = flip(ans)
        return (ans, 1)
    else:
        i1, _ = random.choice(diffs)
        v1Old = ans[i1-1]
        v1New = interact(str(i1))
        bothOrSame = v1Old == v1New
        i1, _ = random.choice(sames)
        v1Old = ans[i1-1]
        v1New = interact(str(i1))
        if bothOrSame:
            if v1Old == v1New:
                # same
                pass
            else:
                # both
                ans = both(ans)
        else:
            # either flipped or reversed
            if v1Old == v1New:
                # reversed
                ans = reverse(ans)
            else:
                # flipped
                ans = flip(ans)
        return (ans, 2)

t, b = getInput()
for i in range(1, t + 1):
    if 'Y' != solve(b):
        break