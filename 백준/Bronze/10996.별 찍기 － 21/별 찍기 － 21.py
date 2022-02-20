n = int(input())
if n == 1:
    print('*')
    exit(0)
content1 = '*' + ' *' * ((n - 1) // 2)
content2 = ' *' * (n // 2)
for i in range(n):
    print(content1)
    print(content2)