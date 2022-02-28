# 11725 트리의 부모 찾기

from sys import stdin as s

input = s.readline

n = int(input())
connection = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)
parents = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
start = [1]
while start:
    new_start = []
    for now in start:
        for can_go in connection[now]:
            if not visited[can_go]:
                parents[can_go] = now
                visited[can_go] = True
                new_start.append(can_go)
    start = new_start
for i in parents[2:]:
    print(i)
