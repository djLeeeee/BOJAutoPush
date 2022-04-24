from sys import stdin

input = stdin.readline

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())


def line(x, y, xx, yy):
    return yy - y, x - xx, xx * y - x * yy


def check(l, x, y, xx, yy):
    if (l[0] * x + l[1] * y + l[2]) * (l[0] * xx + l[1] * yy + l[2]) >= 0:
        return False
    return True


if check(line(x1, y1, x2, y2), x3, y3, x4, y4) and check(line(x3, y3, x4, y4), x1, y1, x2, y2):
    print(1)
else:
    print(0)
