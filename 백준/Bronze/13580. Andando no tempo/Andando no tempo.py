a, b, c = map(int, input().split())
if a == b or b == c or c == a or a == b + c or b == a + c or c == a + b:
    print('S')
else:
    print('N')