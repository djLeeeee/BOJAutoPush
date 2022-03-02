from sys import stdin as s
from itertools import permutations

n, m = map(int, s.readline().split())
num = list(map(int, s.readline().split()))
x = list(permutations(num, m))
x = list(set(x))
x.sort()
for i in x:
    print(*i)