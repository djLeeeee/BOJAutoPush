from sys import stdin as s

input = s.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    print(n - 1)
