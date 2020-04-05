def getInput():
    return input()

def solve(digits):
    prev = '0'
    stack = []
    for d in '0' + digits:
        if prev != d:
            if prev < d:
                stack.append('(' * (int(d) - int(prev)))
            else:
                stack.append(')' * (int(prev) - int(d)))
            prev = d
        stack.append(d)
    if stack:
        stack.append(')' * int(stack[-1]))
    return ''.join(stack[1:])

t = int(input())
for i in range(1, t + 1):
    digits = getInput()
    print("Case #{}: {}".format(i, solve(digits)))