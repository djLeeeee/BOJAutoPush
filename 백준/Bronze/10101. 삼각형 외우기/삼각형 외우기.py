a = [int(input()) for _ in range(3)]
b = set(a)
if sum(a) == 180:
    if len(b) == 1:
        print('Equilateral')
    elif len(b) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
