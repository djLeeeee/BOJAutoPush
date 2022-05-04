a, b = int(input()), int(input())
if b + 60 >= a:
    print(a * 1500)
else:
    print(a * 3000 - (b + 60) * 1500)
