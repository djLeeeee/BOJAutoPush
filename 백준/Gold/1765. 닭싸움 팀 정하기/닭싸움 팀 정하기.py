from sys import stdin

input = stdin.readline


def find(target):
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]


n = int(input())
parent = list(range(n + 1))
ans = n
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, x, y = input().split()
    x, y = int(x), int(y)
    if s == 'E':
        py = find(y)
        for xx in graph[x]:
            pxx = find(xx)
            if pxx != py:
                ans -= 1
                parent[pxx] = py
        px = find(x)
        for yy in graph[y]:
            pyy = find(yy)
            if pyy != px:
                ans -= 1
                parent[pyy] = px
        graph[x].append(y)
        graph[y].append(x)
    else:
        px, py = find(x), find(y)
        if px != py:
            ans -= 1
            parent[px] = py
print(ans)

