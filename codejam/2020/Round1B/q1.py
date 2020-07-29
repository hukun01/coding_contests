rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(x, y):
    xFlipped = x < 0
    yFlipped = y < 0
    if xFlipped:
        x = -x
    if yFlipped:
        y = -y
    if x % 2 == y % 2:
        return "IMPOSSIBLE"

    maps = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
    def check(x, y, goback):
        steps = []
        if x % 2 == 1:
            if goback:
                steps.append('W')
                x += 1
            else:
                steps.append('E')
                x -= 1
        else:
            if goback:
                steps.append('S')
                y += 1
            else:
                steps.append('N')
                y -= 1
        print(f"x: {x}, y: {y}")
        i = 1
        #print(f"updated x: {x}, y: {y}")
        while x > 0 or y > 0:
            if x & (1 << i):
                steps.append('E')
                x &= ~(1 << i)
                if y & (1 << i):
                    steps.append('S')
                    y += (1 << i)
            else:
                if y & (1 << i):
                    y &= ~(1 << i)
                    steps.append('N')
                else:
                    #print("xxx")
                    return "IMPOSSIBLE"
            x = x >> 1
            y = y >> 1
        # handle flips
        if xFlipped:
            for i in range(len(steps)):
                if steps[i] in 'EW':
                    steps[i] = maps[steps[i]]
        if yFlipped:
            for i in range(len(steps)):
                if steps[i] in 'SN':
                    steps[i] = maps[steps[i]]
        return ''.join(steps)
    check1 = check(x, y, True)
    if check1 == "IMPOSSIBLE":
        return check(x, y, False)
    return check1

for i in range(1, rri() + 1):
    x, y = rrm()
    print("Case #{}: {}".format(i, solve(x, y)))