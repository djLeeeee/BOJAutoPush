from sys import stdin as s
from sys import setrecursionlimit as st

st(10 ** 9)
p = 1000000007


def multiple(first, second):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += first[i][k] * second[k][j]
            result[i][j] %= p
    return result


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    return gcd(a - b, b)


n, m = map(int, s.readline().split())
t = gcd(n, m) - 1
x = [[1, 0], [0, 1]]
matrix = [[1, 1], [1, 0]]
while t > 0:
    if t & 1:
        x = multiple(x, matrix)
    t >>= 1
    matrix = multiple(matrix, matrix)
print(x[0][0])
