import random
R = 100
C = 1000
T = 10
print(T)
for _ in range(T):
    print("{} {}".format(R, C))
    for r in range(R):
        line = []
        for c in range(C):
            line.append(random.randint(1, 1000000))
        print(' '.join(str(e) for e in line))