from sys import stdin

input = stdin.readline

for tc in range(1, int(input()) + 1):
    n = int(input())
    foods = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0] * (1 << n)
    point = [0]
    for _ in range(n):
        new = set()
        for c in point:
            for bit in range(n):
                if not (1 << bit) & c:
                    now = c + (1 << bit)
                    new.add(now)
                    if dp[c] <= foods[bit][0]:
                        if dp[now] < dp[c] + foods[bit][1]:
                            dp[now] = dp[c] + foods[bit][1]
        point = new
    print(f'Case #{tc}: {max(dp)}')
