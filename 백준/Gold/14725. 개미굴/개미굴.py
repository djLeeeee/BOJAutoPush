from sys import stdin
from collections import deque, defaultdict

input = stdin.readline


def sol(edges, depth):
    if not edges[0]:
        return []
    children = defaultdict(list)
    for edge in edges:
        x = edge.popleft()
        children[x].append(edge)
    nodes = sorted(children)
    ans = []
    for node in nodes:
        ans += [(node, depth)] + sol(children[node], depth + 1)
    return ans


n = int(input())
tree = []
for _ in range(n):
    _, *path = input().strip().split()
    tree.append(deque(path))
tree.sort()
result = sol(tree, 0)
for value, d in result:
    print('--' * d + value)
