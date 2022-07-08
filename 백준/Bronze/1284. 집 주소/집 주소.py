from sys import stdin

input = stdin.readline

while True:
    n = input().rstrip()
    if n == '0':
        break
    ans = len(n) * 1 + 1
    for c in n:
        if c == '0':
            ans += 4
        elif c == '1':
            ans += 2
        else:
            ans += 3
    print(ans)
