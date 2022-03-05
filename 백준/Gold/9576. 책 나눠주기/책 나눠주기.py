import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def dfs(start):
    x, y = graph[start]
    for adj in range(x, y + 1):
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = start
            return True
    return False


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    match = [-1] * (n + 1)
    for i in range(m):
        visited = [False] * (n + 1)
        dfs(i)
    print(sum([1 for j in match if j >= 0]))
