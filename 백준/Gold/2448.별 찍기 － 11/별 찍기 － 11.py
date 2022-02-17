def triangle(num):
    if num == 3:
        return ['*', '* *', '*****']
    hole = [' ' * i for i in range(num - 1, 0, -2)]
    small = triangle(num // 2)
    result = [0] * (num // 2)
    for i in range(num // 2):
        result[i] = small[i] + hole[i] + small[i]
    return small + result


n = int(input())
stars = triangle(n)
for j in range(n):
    print(' ' * (n - j - 1), end='')
    print(stars[j], end='')
    print(' ' * (n - j - 1))