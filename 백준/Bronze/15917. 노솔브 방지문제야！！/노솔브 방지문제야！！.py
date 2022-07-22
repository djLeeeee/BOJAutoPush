from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    i = int(input())
    while i > 1:
        if i % 2:
            break
        i //= 2
    print(1 if i == 1 else 0)
