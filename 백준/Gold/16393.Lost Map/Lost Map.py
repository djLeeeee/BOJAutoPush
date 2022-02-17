from sys import stdin as s
from sys import setrecursionlimit as strc
strc(10 ** 6)

n = int(s.readline())

parent = list(range(n + 1))

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

connection = [ ]
for i in range(1, n + 1):
    a = list(map(int, s.readline().split()))
    for j in range(n - i):
        connection.append([-a[i + j], i, i + j + 1])

connection.sort()

v = 0
result = [ ]
while v < n - 1:
    line = connection.pop()
    if find(line[1]) != find(line[2]):
        v += 1
        union(line[1], line[2])
        print(line[1], line[2])