from sys import stdin as s
from sys import setrecursionlimit as st

input = s.readline
st(10 ** 4)


def dfs(start):
    for adj in graph[start]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = start
            return True
    return False


n, k, t1, t2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(t1):
    x, y = map(int, input().split())
    graph[x].append(y)
match = [0] * (k + 1)
for i in range(1, n + 1):
    visited = [False] * (k + 1)
    dfs(i)
a = sum([1 for j in match if j > 0])
graph = [[] for _ in range(n + 1)]
for _ in range(t2):
    x, y = map(int, input().split())
    graph[x].append(y)
match = [0] * (k + 1)
for i in range(1, n + 1):
    visited = [False] * (k + 1)
    dfs(i)
b = sum([1 for j in match if j > 0])
if a < b:
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')
