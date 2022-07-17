from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def sol(idx):

    def search(edge_idx):
        if memo[edge_idx]:
            return memo[edge_idx]
        s, e = edge[edge_idx]
        if not graph[e] or graph[e][-1] < edge_idx:
            memo[edge_idx] = e
            return e
        start = 0
        end = len(graph[e]) - 1
        while start <= end:
            mid = (start + end) // 2
            if graph[e][mid] >= edge_idx:
                result = graph[e][mid]
                end = mid - 1
            else:
                start = mid + 1
        memo[edge_idx] = search(result)
        return memo[edge_idx]

    if not graph[idx]:
        return idx
    return search(graph[idx][0])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edge = []
memo = [0] * m
for i in range(m):
    x, y = map(int, input().split())
    edge.append((x, y))
    graph[x].append(i)
print(*[sol(i) for i in range(1, n + 1)])
