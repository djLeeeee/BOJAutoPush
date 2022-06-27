from sys import stdin

input = stdin.readline

n = int(input())
stack = [int(input())]
ans = 0
for _ in range(n - 1):
    m = int(input())
    if stack[0] > m:
        while stack and stack[-1] <= m:
            stack.pop()
            ans += min(stack[-1], m)
    else:
        ans += sum(stack[:-1])
        stack = [m]
    stack.append(m)
print(ans + sum(stack[:-1]))
