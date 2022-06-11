from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
ans = n + m
a = set(map(int, input().split()))
b = set(map(int, input().split()))
for c in a:
    if c in b:
        ans -= 2
print(ans)
