from sys import stdin
from itertools import combinations

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    for orders in list(combinations(list(range(n)), n // 2)):
        now = [0, 0]
        for i in range(n):
            if i in orders:
                now[0] += arr[i][0]
                now[1] += arr[i][1]
            else:
                now[0] -= arr[i][0]
                now[1] -= arr[i][1]
        res = now[0] ** 2 + now[1] ** 2
        if res < ans:
            ans = res
    print(ans ** 0.5)
