n = int(input())
k = n // 2 + 1
if n % 2:
    print(k * k + k)
else:
    print(k * k)
