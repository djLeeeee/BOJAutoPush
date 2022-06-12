from sys import stdin

input = stdin.readline

p1, q1, p2, q2 = map(int, input().split())
print(0 if (p1 * p2) % (q1 * q2 * 2) else 1)
