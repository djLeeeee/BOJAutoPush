from sys import stdin as s

n, m, k = map(int, s.readline().split())
cost = [0] + list(map(int, s.readline().split()))
parents = list(range(n + 1))


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]


def union(a, b):
    p = find(a)
    q = find(b)
    if p < q:
        parents[q] = p
    else:
        parents[p] = q
    return


for _ in range(m):
    x, y = map(int, s.readline().split())
    union(x, y)
optimize_cost = {}
for i in range(1, n + 1):
    try:
        optimize_cost[find(i)] = min(optimize_cost[find(i)], cost[i])
    except:
        optimize_cost[find(i)] = cost[i]
x = sum(optimize_cost.values())
if k >= x:
    print(x)
else:
    print('Oh no')
