coins = [25, 10, 5, 1]
for _ in range(int(input())):
    ans = []
    t = int(input())
    for coin in coins:
        ans.append(t // coin)
        t %= coin
    print(*ans)