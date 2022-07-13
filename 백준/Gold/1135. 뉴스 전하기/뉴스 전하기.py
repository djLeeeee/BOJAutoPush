def sol(idx):
    if not graph[idx]:
        return 0
    call_time = [sol(adj) for adj in graph[idx]]
    call_time.sort()
    l = len(call_time)
    result = 0
    for ex in range(l):
        if result < l - ex + call_time[ex]:
            result = l - ex + call_time[ex]
    return result


n = int(input())
graph = [[] for _ in range(n + 1)]
for i, j in enumerate(map(int, input().split())):
    graph[j].append(i)
print(sol(0))
