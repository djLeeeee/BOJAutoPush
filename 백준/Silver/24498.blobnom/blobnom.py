n = int(input())
array = list(map(int, input().split()))
ans = max(array)
if n <= 2:
    print(max(array))
else:
    for i in range(1, n - 1):
        ans = max(ans, array[i] + min(array[i - 1], array[i + 1]))
    print(ans)
