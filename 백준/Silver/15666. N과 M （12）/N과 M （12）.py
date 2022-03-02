from sys import stdin as s
from itertools import combinations_with_replacement as cr

m, n = map(int, s.readline().split())
my_list = [int(i) for i in s.readline().split()]
my_list = list(set(my_list))
my_list.sort()
a = cr(my_list, n)
for i in a:
    print(*i, sep = ' ')