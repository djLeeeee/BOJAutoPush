while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a + c == 2 * b:
        print('AP', c + b - a)
    else:
        print('GP', c * b // a)
