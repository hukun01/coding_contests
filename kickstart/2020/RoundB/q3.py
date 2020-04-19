rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve():
    s = rr()
    stack = [[1, 0, 0]] # multiplier, south diff, east diff
    i = 0
    n = len(s)
    while i < n:
        if s[i].isdigit():
            stack.append([int(s[i:i+1]), 0, 0])
        else:
            #print("stack: ", stack)
            if s[i] == ')':
                count, so, ea = stack.pop()
                stack[-1][1] += so * count
                stack[-1][2] += ea * count
            else:
                if s[i] in 'SN':
                    stack[-1][1] += 1 if s[i] == 'S' else -1
                if s[i] in 'EW':
                    stack[-1][2] += 1 if s[i] == 'E' else -1
        i += 1
    count, south, east = stack.pop()
    south *= count
    east *= count
    boundary = 10 ** 9
    south = south % boundary
    if south < 0:
        south += boundary
    east = east % boundary
    if east < 0:
        east += boundary
    return (east + 1, south + 1)

for i in range(1, rri() + 1):
    print("Case #{}: {} {}".format(i, *solve()))