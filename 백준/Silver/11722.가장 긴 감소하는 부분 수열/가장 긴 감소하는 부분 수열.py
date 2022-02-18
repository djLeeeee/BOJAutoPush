from sys import stdin as s

n = int(s.readline())
array = list(map(int, s.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))