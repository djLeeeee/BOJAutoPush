n = int(input())
price = [list(map(int, input())) for _ in range(n)]
dist = [[float('inf')] * n for _ in range(1 << n)]
point = [(1, 0)]
dist[1][0] = 0
ans = 0
flag = True
while flag:
    ans += 1
    flag = False
    new = set()
    for state, last in point:
        for bit in range(n):
            if not (1 << bit) & state:
                if dist[state + (1 << bit)][bit] > price[last][bit] >= dist[state][last]:
                    flag = True
                    dist[state + (1 << bit)][bit] = price[last][bit]
                    new.add((state + (1 << bit), bit))
    point = new
print(ans)
