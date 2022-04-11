from sys import stdin

input = stdin.readline

a = 0
b = 0
for _ in range(int(input())):
    o, *n = map(int, input().split())
    if o == 1:
        a += n[0]
        b ^= n[0]
    elif o == 2:
        a -= n[0]
        b ^= n[0]
    elif o == 3:
        print(a)
    else:
        print(b)
