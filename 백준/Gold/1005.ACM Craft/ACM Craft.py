from sys import stdin as s
from collections import deque

T = int(s.readline())

for _ in range(T):
    n, k  = map(int, s.readline().split())
    time = [0] + list(map(int, s.readline().split()))
    connection = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)
    get_in = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, s.readline().split())
        connection[x].append(y)
        get_in[y] += 1
    leaves = deque()
    for i in range(1, n + 1):
        if get_in[i] == 0:
            leaves.append(i)
            dp[i] = time[i]
    while leaves:
        a = leaves.popleft()
        for j in connection[a]:
            dp[j] = max(dp[j], dp[a] + time[j])
            get_in[j] -= 1
            if get_in[j] == 0:
                leaves.append(j)
    print(dp[int(s.readline())])