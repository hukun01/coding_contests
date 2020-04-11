def getInput():
    n = int(input())
    ps = []
    for _ in range(n):
        ps.append(list(input()))
    return ps

def solve(ps):
    def preprocess(ps):
        processed = set()
        for p in ps:
            start = 0
            while start < len(p) and p[start] != '*':
                start += 1
            end = len(p) - 1
            while end >= 0 and p[end] != '*':
                end -= 1
            for i in range(start + 1, end):
                if p[i] == '*':
                    p[i] = '#'
            processed.add(''.join(x for x in p if x != '#'))
        return processed
    ps = preprocess(ps)
    print(ps)
    heads = set()
    tails = set()
    middles = set()
    for p in ps:
        if p:
            if p[0] == '*':
                if p[-1] == '*':
                    middles.add(p)
                else:
                    tails.add(p)
            else:
                heads.add(p)
                if p[-1] != '*':
                    tails.add(p)
    
    def check(parts):
        print("checking parts: ", parts)
        if not parts:
            return (True, "")
        idxs = [0] * len(parts)
        longestHead = []
        while True:
            chars = set()
            for idx in range(len(parts)):
                chars.add(parts[idx][idxs[idx]])
                if idx < len(idxs) and idxs[idx] != '*':
                    idxs[idx] += 1
            chars.discard('*')
            if len(chars) > 1:
                return (False, "")
            if chars:
                longestHead.append(chars.pop())
            else:
                break
        return (True, ''.join(longestHead))

    isGood, head = check(list(heads))
    if not isGood:
        return '*'
    isGood, tail = check([t[::-1] for t in tails])
    if not isGood:
        return '*'
    tail = tail[::-1]

    wc = dict()
    mid = ""
    if middles:
        for c in middles.pop():
            if c not in wc:
                wc[c] = 1
            else:
                wc[c] += 1
        for m in middles:
            wc1 = dict()
            for c in m:
                if c not in wc1:
                    wc1[c] = 1
                else:
                    wc1[c] += 1
            for c, count in wc1.items():
                if c not in wc:
                    wc[c] = count
                elif count > wc:
                    wc[c] = count
        mids = []
        for c, count in wc.items():
            mids.append(c * count)
        mid = ''.join(mids)
    return head + mid +  tail

t = int(input())
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve(getInput())))