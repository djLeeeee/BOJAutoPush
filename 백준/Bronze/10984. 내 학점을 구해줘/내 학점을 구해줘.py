from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    s, t = 0, 0
    for _ in range(int(input())):
        a, b = map(float, input().split())
        s += a * b
        t += a
    print(int(t), s / t)
