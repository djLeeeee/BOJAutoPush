from sys import stdin

input = stdin.readline

n = int(input())
tower = list(map(int, input().split()))
ans = [0] * n
stack = [(10 ** 8 + 1, 0)]
for i in range(n):
    h = tower[i]
    while stack[-1][0] < h:
        stack.pop()
    ans[i] = stack[-1][1]
    stack.append((h, i + 1))
print(*ans)
