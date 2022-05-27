from sys import stdin

input = stdin.readline

a, x, b, y, t = [int(input()) for _ in range(5)]
if t > 30:
    a += (t - 30) * x * 21
if t > 45:
    b += (t - 45) * y * 21
print(a, b)
