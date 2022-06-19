from sys import stdin
from random import randint

input = stdin.readline


def check(t):
    A = [list(map(int, input().split())) for _ in range(t)]
    B = [list(map(int, input().split())) for _ in range(t)]
    for _ in range(20):
        v = [randint(0, 1) for _ in range(t)]
        v1, v2, v3 = [0] * t, [0] * t, [0] * t
        for i in range(t):
            for j in range(t):
                v1[i] += A[i][j] * v[j]
        for i in range(t):
            for j in range(t):
                v2[i] += A[i][j] * v1[j]
        for i in range(t):
            for j in range(t):
                v3[i] += B[i][j] * v[j]
            if v3[i] != v2[i]:
                return "NO"
    return "YES"


while True:
    n = int(input())
    if n:
        print(check(n))
        input()
    else:
        break
