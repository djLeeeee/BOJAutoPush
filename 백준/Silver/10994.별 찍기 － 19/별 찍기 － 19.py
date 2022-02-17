def strange_square(n):
    if n == 1:
        return ['*']
    border = ['*' * (4 * n - 3)]
    padding = ['*' + ' ' * (4 * n - 5) + '*']
    content = [0] * (4 * n - 7)
    x = strange_square(n - 1)
    for i in range(4 * n - 7):
        content[i] = '* ' + x[i] + ' *'
    return border + padding + content + padding + border


for line in strange_square(int(input())):
    print(line)
