rr = input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split(' '))

def solve(c1, r1, c2, r2, c3, r3):
    # (c1-1, r1-1) is the target
    # (c2-1, r2-1) ~ (c3-1, r3-1) inclusive, is the hole
    # robot only goes right or down.
    if c1 > r1:
        c1, r1, c2, r2, c3, r3 = r1, c1, r2, c2, r3, c3

    def inHole(r, c):
        return r2-1 <= r <= r3-1 and c2-1 <= c <= c3-1

    f = [0] * c1
    f[0] = 1.0
    for c in range(1, c1):
        f[c] = f[c-1] * (0.5 if not inHole(0, c) else 0)
    #print(f)
    
    for r in range(1, r1):
        f[0] *= 0.5 if not inHole(r, 0) else 0
        for c in range(1, c1):
            if inHole(r, c):
                f[c] = 0
                continue
            if r == r1 - 1 and c == c1 - 1:
                f[c] += f[c-1]
                #f[c] += f[r][c - 1]
            elif r != r1 - 1:
                if c == c1 - 1:
                    f[c] = f[c] + 0.5 * f[c-1]
                    #f[r][c] += f[r-1][c] + 0.5 * f[r][c-1]
                else:
                    f[c] = 0.5 * (f[c] + f[c-1])
                    #f[r][c] += 0.5 * (f[r-1][c] + f[r][c-1])
            else:
                if r == r1 - 1:
                    f[c] = 0.5 * f[c] + f[c-1]
                    #f[r][c] += 0.5 * f[r-1][c] + f[r][c-1]
                else:
                    f[c] = 0.5 * (f[c] + f[c-1])
                    #f[r][c] += 0.5 * (f[r-1][c] + f[r][c-1])
        #print(f)
    #print(f)
    return f[-1]

for i in range(1, rri() + 1):
    W, H, L, U, R, D = rrm()
    print("Case #{}: {}".format(i, solve(W, H, L, U, R, D)))