n = int(input())
content = '*' + ' *' * (n - 1)
for i in range(n):
    if i % 2:
        print('', content)
    else:
        print(content)
