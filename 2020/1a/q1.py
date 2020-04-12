from collections import deque
rr = input
rri = lambda: int(rr())
rrl = lambda: rr().split()
rrm = lambda: list(map(int, rrl))

def solve(A):
    A = [deque(word.split('*')) for word in A]
    prefix = ""
    suffix = ""
    for row in A:
        head = row.popleft()
        tail = row.pop()
        if len(head) > len(prefix):
            if not head.startswith(prefix):
                return '*'
            prefix = head
        else:
            if not prefix.startswith(head):
                return '*'
        if len(tail) > len(suffix):
            if not tail.endswith(suffix):
                return '*'
            suffix = tail
        else:
            if not suffix.endswith(tail):
                return '*'

    return "".join([prefix] + ["".join(middle) for middle in A] + [suffix])

t = int(input())
for i in range(1, t + 1):
    A = [rr() for _ in range(rri())]
    print("Case #{}: {}".format(i, solve(A)))