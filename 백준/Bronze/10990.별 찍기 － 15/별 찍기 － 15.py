n = int(input())
print(' ' * (n - 1) + '*')
x = n - 2
y = 1
for i in range(1, n):
    print(' ' * x + '*' + ' ' * y + '*')
    x -= 1
    y += 2
