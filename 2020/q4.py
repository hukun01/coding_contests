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

def getRandomIndexPair(candidates, b):
    i1 = random.sample(candidates, 1)[0] if len(candidates) > 0 else 1
    candidates.remove(i1)
    i2 = b + 1 - i1
    return i1, i2

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

    Once we know what operation happened on the array in DB, we can apply the
    same operation to the array in our hands to keep data in sync.
    '''
    ROUND = 10
    MAX_QUERIES_COUNT = 150

    sames = [] # the index pairs at which the values are the same
    diffs = [] # the index pairs at which the values are different
    ans = [''] * b

    indicies = list(range(1, b // 2 + 1))
    random.shuffle(indicies)

    queryCount = 0
    for limit in range(ROUND, MAX_QUERIES_COUNT, ROUND):
        while queryCount + 2 <= limit and indicies:
            queryCount += 2
            i1 = indicies.pop()
            i2 = b + 1 - i1
            ans[i1-1] = interact(str(i1))
            ans[i2-1] = interact(str(i2))
            if ans[i1-1] == ans[i2-1]:
                sames.append((i1, i2))
            else:
                diffs.append((i1, i2))
        if not indicies:
            break

        ans = update(ans, diffs, sames)
        queryCount += 2
    return interact(''.join(ans))

def update(ans, diffs, sames):
    '''
    Determine the transformation operation: any of [same, flip, reverse, both].
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
        # Now we have incremented the query by 1, and we intentionally waste this query
        # below to keep the query pace consistent.
        # Note that now we don't want to retrieve any index pair from the total indicies,
        # because that would make the query count incremented by 3.
        _ = interact(str(i1))
    else:
        '''
        Check an index from a diff pair and a same pair, respectively.
        In the diff pair: 
        1. If the value remains the same, the operation was either 'both' or 'same'.
        Now check the same pair:
            a. If the value remains the same, the operation was 'same';
            b. Otherwise, the operation was 'both'.
        2. otherwise operation was 'flip' or 'reverse'.
        Now check the same pair:
            a. If the value remains the same, the operation was 'reverse';
            b. Otherwise, the operation was 'flip'.
        '''
        i1, _ = random.choice(diffs)
        v1Old = ans[i1-1]
        v1New = interact(str(i1))
        bothOrSame = v1Old == v1New
        i2, _ = random.choice(sames)
        v2Old = ans[i2-1]
        v2New = interact(str(i2))
        if bothOrSame:
            if v2Old == v2New:
                pass
            else:
                ans = both(ans)
        else:
            # either flipped or reversed
            if v2Old == v2New:
                ans = reverse(ans)
            else:
                ans = flip(ans)
    return ans

t, b = getInput()
for i in range(1, t + 1):
    if 'Y' != solve(b):
        break