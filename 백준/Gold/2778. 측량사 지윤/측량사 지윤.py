from sys import stdin

input = stdin.readline


def intersection(e1, e2):
    a1, b1, c1 = e1
    a2, b2, c2 = e2
    if a1 * b2 - a2 * b1 == 0:
        return False
    return (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1), (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)


n = int(input())
for i in range(n):
    equation = [tuple(map(int, input().split())) for _ in range(3)]
    p1 = intersection(equation[0], equation[1])
    p2 = intersection(equation[1], equation[2])
    p3 = intersection(equation[2], equation[0])
    if p1 and p2 and p3:
        x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
        x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
        ans = abs(x1 * y2 - x2 * y1) / 2
    else:
        ans = 0
    print('{:.4f}'.format(ans))
