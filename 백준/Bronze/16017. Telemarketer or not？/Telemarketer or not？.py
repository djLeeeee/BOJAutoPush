a = [int(input()) for _ in range(4)]
if a[0] not in [8, 9] or a[-1] not in [8, 9] or a[1] != a[2]:
    print('answer')
else:
    print('ignore')
