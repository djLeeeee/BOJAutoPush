from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m, k = map(int, input().split())
bbok_love = [[] for _ in range(n + 1)]
bbok_hate = [[] for _ in range(n + 1)]
kkok_love = [[] for _ in range(m + 1)]
kkok_hate = [[] for _ in range(m + 1)]
bn = 0
kn = 0
for _ in range(k):
    x, y, case = map(int, input().split())
    if case:
        kn += 1
        kkok_love[y].append(kn)
        bbok_hate[x].append(kn)
    else:
        bn += 1
        bbok_love[x].append(bn)
        kkok_hate[y].append(bn)
graph = [[] for _ in range(bn + 1)]
for i in range(1, n + 1):
    for li in bbok_love[i]:
        for hi in bbok_hate[i]:
            graph[li].append(hi)
for i in range(1, m + 1):
    for hi in kkok_hate[i]:
        for li in kkok_love[i]:
            graph[hi].append(li)
ans = 0
match = [0] * (kn + 1)
for i in range(1, bn + 1):
    visited = [False] * (kn + 1)
    ans += dfs(i)
print(ans)
