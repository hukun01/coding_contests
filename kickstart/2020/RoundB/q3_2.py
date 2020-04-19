import collections
rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve():
    s = rr()
    stack = [[1, ""]]
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and s[j].isdigit():
            j += 1
        if j > i:
            stack.append([int(s[i:j]), ""])
            i = j + 1
        else:
            #print("stack: ", stack)
            if s[i] == ')':
                count, part = stack.pop()
                stack[-1][1] += part * count
            else:
                stack[-1][1] += s[i]
            i += 1
    count, part = stack.pop()
    program = part * count
    counter = collections.Counter(program)
    boundary = 10 ** 9
    south = counter['S'] - counter['N']
    if south < 0:
        south += boundary
    east = counter['E'] - counter['W']
    if east < 0:
        east += boundary
    return (1 + east, 1 + south)

for i in range(1, rri() + 1):
    print("Case #{}: {} {}".format(i, *solve()))