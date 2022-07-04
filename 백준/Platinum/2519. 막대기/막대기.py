from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def draw_or_edge(a, b):
    graph[-a].append(b)
    graph[-b].append(a)


def line(a, b, c, d):
    return d - b, a - c, b * c - a * d


def check(l, a, b, c, d):
    if (l[0] * a + l[1] * b + l[2]) * (l[0] * c + l[1] * d + l[2]) > 0:
        return False
    return True


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if scc[idx]:
        return
    scc[idx] = component
    if scc[-idx] == component:
        print(-1)
        exit()
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n = int(input())
graph = [[] for _ in range(6 * n + 1)]
x, y, z = 1, 2, 3
for _ in range(n):
    draw_or_edge(-x, -y)
    draw_or_edge(-y, -z)
    draw_or_edge(-z, -x)
    x += 3
    y += 3
    z += 3
stick = [0]
for i in range(1, 3 * n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    now = line(x1, y1, x2, y2)
    for j in range(1, i):
        x3, y3, x4, y4 = stick[j]
        past = line(x3, y3, x4, y4)
        if check(now, x3, y3, x4, y4) and check(past, x1, y1, x2, y2):
            draw_or_edge(i, j)
    stick.append((x1, y1, x2, y2))
visited = [False] * (6 * n + 1)
stack = []
for i in range(1, 3 * n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = [0] * (6 * n + 1)
component = 0
ans = []
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
cnt = 0
ans = []
for i in range(n):
    for ex in range(1, 4):
        now = i * 3 + ex
        if scc[-now] < scc[now]:
            cnt += 1
            ans.append(now)
            break
print(cnt)
print(*ans)
