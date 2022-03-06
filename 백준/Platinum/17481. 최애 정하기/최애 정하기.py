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
index = {input().rstrip(): i for i in range(m)}
graph = [[] for _ in range(n)]
for j in range(n):
    a = input().strip().split()
    for name in a[1:]:
        graph[j].append(index[name])
match = [-1] * m
for k in range(n):
    visited = [False] * m
    dfs(k)
pair = sum([1 for p in match if p >= 0])
if pair == n:
    print('YES')
else:
    print('NO')
    print(pair)
