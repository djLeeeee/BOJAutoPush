def no_more_recursion(n):
    if n == 2:
        return ['*****', '*', '* ***', '* * *', '* * *', '*   *', '*****']
    x = no_more_recursion(n - 1)
    x[1] = '*' + ' ' * (4 * n - 8)
    content = [0] * (4 * n - 5)
    content[0] = '* ' + x[0] + '**'
    for i in range(1, 4 * n - 5):
        content[i] = '* ' + x[i] + ' *'
    return ['*' * (4 * n - 3), '*'] + content + ['*' + ' ' * (4 * n - 5) + '*', '*' * (4 * n - 3)]


idx = int(input())
if idx == 1:
    print('*')
else:
    result = no_more_recursion(idx)
    for line in result:
        print(line)