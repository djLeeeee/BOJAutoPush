ans = -1
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x <= y:
        if ans == -1 or ans > y:
            ans = y
print(ans)
