from collections import defaultdict

vertex = defaultdict(bool)
edge = defaultdict(bool)
n = int(input())
v = 1
e = 0
vertex[(0, 0)] = True
order = input()
x, y = 0, 0
d = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}
for o in order:
    dx, dy = d[o]
    if not vertex[(x + dx, y + dy)]:
        v += 1
        vertex[(x + dx, y + dy)] = True
    if not edge[(x, y, x + dx, y + dy)]:
        e += 1
        edge[(x, y, x + dx, y + dy)] = True
        edge[(x + dx, y + dy, x, y)] = True
    x += dx
    y += dy
print(1 - v + e)
