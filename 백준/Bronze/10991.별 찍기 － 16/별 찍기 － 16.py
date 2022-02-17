n = int(input())
print(' ' * (n - 1) + '*')
x = n - 2
for i in range(1, n):
    print(' ' * x + '*' + ' *' * i)
    x -= 1
