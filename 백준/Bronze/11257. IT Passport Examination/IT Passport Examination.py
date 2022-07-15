for _ in range(int(input())):
    x, a, b, c = map(int, input().split())
    ans = 'FAIL'
    if a * 2 >= 21 and b * 2 >= 15 and c >= 12 and a + b + c >= 55:
        ans = 'PASS'
    print(f'{x} {a + b + c} {ans}')
