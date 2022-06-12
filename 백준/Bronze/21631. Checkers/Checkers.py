from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
m -= 1
print(1 + min(n, m))
