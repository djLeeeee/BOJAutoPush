from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())
my_dic = defaultdict(int)
for _ in range(n):
    my_dic[input().rstrip()] += 1
ans = 0
for _ in range(m):
    ans += my_dic[input().rstrip()]
print(ans)