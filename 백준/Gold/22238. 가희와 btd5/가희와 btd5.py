from sys import stdin
from collections import defaultdict
from math import gcd

input = stdin.readline

n, m = map(int, input().split())
balloon = defaultdict(list)
for _ in range(n):
    x, y, h = map(int, input().split())
    z = gcd(x, y)
    x //= z
    y //= z
    balloon[(x, y)].append(h)
for key in balloon:
    balloon[key].sort(reverse=True)
ans = n
attack = defaultdict(int)
for _ in range(m):
    x, y, a = map(int, input().split())
    z = gcd(x, y)
    x //= z
    y //= z
    attack[(x, y)] += a
    while balloon[(x, y)] and balloon[(x, y)][-1] <= attack[(x, y)]:
        balloon[(x, y)].pop()
        ans -= 1
    print(ans)
