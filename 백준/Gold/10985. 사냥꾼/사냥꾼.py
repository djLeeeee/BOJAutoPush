from sys import stdin
from math import acos

input = stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2, r = map(float, input().split())
    xy1 = x1 * x1 + y1 * y1
    xy2 = x2 * x2 + y2 * y2
    xy = (x2 - x1) ** 2 + (y2 - y1) ** 2
    yx = x1 * y2 - x2 * y1
    if x1 == x2 and y1 == y2:
        ans = 0
    else:
        d = abs(yx) / (xy ** 0.5)
        if d >= r:
            ans = xy ** 0.5
        else:
            t = yx * (y2 - y1) / xy
            if (x1 <= t and x2 <= t) or (x1 >= t and x2 >= t):
                ans = xy ** 0.5
            else:
                r1 = acos(r / xy1 ** 0.5) + acos(r / xy2 ** 0.5)
                r2 = acos((xy1 + xy2 - xy) / (2 * xy1 ** 0.5 * xy2 ** 0.5))
                ans = (xy1 - r * r) ** 0.5 + (xy2 - r * r) ** 0.5 + (r2 - r1) * r
    print('{:.3f}'.format(round(ans, 3)))
