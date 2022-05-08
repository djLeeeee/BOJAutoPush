from sys import stdin

input = stdin.readline

n = int(input())
ans = 0
circles = []
for _ in range(n):
    c, r = map(int, input().split())
    circles.append((c - r, c + r))
circles.sort()
stack = []
ans = 'YES'
for s, e in circles:
    while stack and stack[-1][1] < s:
        stack.pop()
    if stack:
        if stack[-1][1] <= e:
            ans = 'NO'
            break
    stack.append((s, e))
print(ans)
