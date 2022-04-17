n = int(input())
m = 5 * n - 400
print(m)
if m > 100:
    print(-1)
elif m < 100:
    print(1)
else:
    print(0)