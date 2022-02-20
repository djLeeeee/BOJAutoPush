from sys import stdin as s

n = int(s.readline())
array = list(map(int, s.readline().split()))
if n == 1:
    print(1)
    print(*array)
else:
    dp = [1] * n
    maxi = 0
    idx = 0
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
            if dp[i] > maxi:
                maxi = dp[i]
                idx = i
    print(maxi)
    ans = [0] * maxi
    i = -1
    while maxi > 0:
        if dp[i] == maxi:
            maxi -= 1
            ans[maxi] = array[i]
        i -= 1
    print(*ans)

