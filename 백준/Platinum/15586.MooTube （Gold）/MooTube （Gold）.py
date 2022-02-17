from sys import stdin as s

m, n = map(int, s.readline().split())
usado = [ ]
for i in range(m - 1):
    p, q, r = map(int, s.readline().split())
    usado.append((r, p, q))
usado.sort(reverse = True)
limit = [ ]
origin = [ ]
for j in range(n):
    k, v = map(int, s.readline().split())
    limit.append((k, j))
    origin.append(v)
limit.sort()
parent = list(range(m + 1))
parent_num = [1] * (m + 1)
def find(target):
	if target == parent[target]:
		return target
	parent[target] = find(parent[target])
	return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = [0] * n
i = 0
while limit:
    a = limit.pop()
    limit_now = a[0]
    limit_index = a[1]
    while i <= m - 2 and usado[i][0] >= limit_now:
        x = usado[i][1]
        y = usado[i][2]
        a = parent_num[find(x)] + parent_num[find(y)]
        union(x, y)
        parent_num[find(x)] = a
        i += 1
    result[limit_index] = parent_num[find(origin[limit_index])] - 1
print(*result, sep = '\n')