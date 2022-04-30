from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    if m % 2:
        if n % 2:
            print(1)
        else:
            print(0)
    else:
        n %= (m + 1)
        if n == m:
            print(m)
        elif n % 2:
            print(1)
        else:
            print(0)