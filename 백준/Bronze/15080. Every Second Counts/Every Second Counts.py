def change(h, m, s):
    return h * 3600 + m * 60 + s


x, y = [change(*map(int, input().split(':'))) for _ in '  ']
if x <= y:
    print(y - x)
else:
    print(y - x + 3600 * 24)