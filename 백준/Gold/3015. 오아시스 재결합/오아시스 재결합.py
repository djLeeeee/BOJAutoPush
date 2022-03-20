from sys import stdin

input = stdin.readline


n = int(input())
stack = []
ans = 0
for _ in range(n):
    height = int(input())
    if stack:
        if stack[-1][0] > height:
            ans += 1
            stack.append((height, 1))
        else:
            flag = True
            while stack and stack[-1][0] <= height:
                h, cnt = stack.pop()
                ans += cnt
                if h == height:
                    if stack:
                        ans += 1
                    stack.append((height, cnt + 1))
                    flag = False
                    break
            if flag:
                if stack:
                    ans += 1
                stack.append((height, 1))
    else:
        stack.append((height, 1))
print(ans)
