from sys import stdin

input = stdin.readline

a, b, c = map(int, input().split())
t = (a + b + c) // 3
if b > t:
    print(b + 2 * c - 3 * t)
else:
    print(3 * t - b - 2 * a)
