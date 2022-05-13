n = int(input())
if n == 1:
    print(2)
else:
    ans = 1
    da = 1
    for i in range(1, n + 1):
        ans += da
        if i % 3:
            da += 1
    print(ans)