from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
s1, s2 = 1000, 1000
for _ in range(m):
    x, y = map(int, input().split())
    if s1 > x:
        s1 = x
    if s2 > y:
        s2 = y
if s1 >= 6 * s2:
    print(n * s2)
else:
    r = n % 6
    if s1 <= s2 * r:
        print((n // 6 + 1) * s1)
    else:
        print((n // 6) * s1 + s2 * r)
