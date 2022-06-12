from sys import stdin

input = stdin.readline

a, c, e = map(int, input().split())
x, y, z = map(int, input().split())
ans = 'E'
if y * 2 >= c:
    ans = 'D'
    if y >= c:
        ans = 'C'
        if x * 2 >= a:
            ans = 'B'
            if x >= a:
                ans = 'A'
print(ans)
