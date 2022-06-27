from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def draw_or_edge(a, b):
    graph[-a].append(b)
    graph[-b].append(a)


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
        print("THINKINGFACE")
        exit()
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m = map(int, input().split())
graph = [[] for _ in range(6 * n + 1)]
color_idx = {
    "BLACK": [], "RED": [0], "BLUE": [1], "GREEN": [2],
    "PURPLE": [0, 1], "CYAN": [1, 2], "YELLOW": [0, 2], "WHITE": [0, 1, 2]
}
for _ in range(m):
    query = input().strip().split()
    x, y = map(int, query[:2])
    state, c1, c2 = query[2:]
    for c in range(3):
        i, j = x * 3 - c, y * 3 - c
        if c in color_idx[c1]:
            if c in color_idx[c2]:
                if state == "L":
                    draw_or_edge(i, j)
                elif state == "H":
                    graph[-i].append(i)
                    graph[-j].append(j)
            else:
                if state == "L":
                    graph[i].append(-i)
                    graph[j].append(-j)
                elif state == "H":
                    draw_or_edge(-i, -j)
        elif c in color_idx[c2]:
            print("THINKINGFACE")
            exit()
visited = [False] * (6 * n + 1)
stack = []
for i in range(1, 3 * n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = [0] * (6 * n + 1)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print("ALIEN")
