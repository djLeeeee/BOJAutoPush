from sys import stdin

input = stdin.readline

t = int(input())
for tc in range(1, t + 1):
    print(f'Scenario #{tc}:')
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    if a * a + b * b + c * c == m * m * 2:
        print("yes")
    else:
        print("no")
    if tc != t:
        print()
