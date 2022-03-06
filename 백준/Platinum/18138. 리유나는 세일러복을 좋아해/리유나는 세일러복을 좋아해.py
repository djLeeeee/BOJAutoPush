# 1867 돌멩이 제거
# 술 마시다가 떠올린 아이디어
from sys import stdin as s
from sys import setrecursionlimit as st

input = s.readline
st(10 ** 4)


def dfs(start):
    for adj in graph[start]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = start
            return True
    return False


n, m = map(int, input().split())
up = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(m):
    down = int(input())
    for j in range(n):
        if up[j] / 2 <= down <= up[j] * 3 / 4 or up[j] <= down <= up[j] * 5 / 4:
            graph[j].append(i)
match = [-1] * m
for k in range(n):
    visited = [False] * m
    dfs(k)
print(sum([1 for pair in match if pair >= 0]))
