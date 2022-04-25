from sys import stdin
from collections import defaultdict
from math import gcd

input = stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    x, y = points[i]
    zero_x = 0
    zero_y = 0
    ex = 0
    tan_cnt = defaultdict(int)
    for j in range(n):
        z, w = points[j]
        if x != z:
            if y != w:
                a, b = y - w, z - x
                c = gcd(a, b)
                a //= c
                b //= c
                tan_cnt[(a, b)] += 1
            else:
                zero_x += 1
        else:
            if y != w:
                zero_y += 1
    key = tan_cnt.keys()
    key = list(key)
    for x, y in key:
        ex += tan_cnt[(x, y)] * (tan_cnt[(y, -x)] + tan_cnt[(-y, x)])
    ex //= 2
    ex += zero_x * zero_y
    ans += ex
print(ans)
