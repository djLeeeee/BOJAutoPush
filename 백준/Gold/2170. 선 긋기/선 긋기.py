from sys import stdin

input = stdin.readline

n = int(input())
ans = 0
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
stack = []
for s, e in lines:
    if stack:
        if s <= stack[1]:
            if e > stack[1]:
                stack[1] = e
        else:
            ans += stack[1] - stack[0]
            stack = [s, e]
    else:
        stack = [s, e]
ans += stack[1] - stack[0]
print(ans)
