from sys import stdin as s
from math import ceil

m, M = map(int, s.readline().split())

sq = int(M ** 0.5)
nums = [ 1 ] * (M - m + 1)
n = 2
while n <= sq:
    x = ceil(m / (n * n))
    while x * n * n <= M:
        nums [x * n * n - m] = 0
        x += 1
    n += 1
print(sum(nums))