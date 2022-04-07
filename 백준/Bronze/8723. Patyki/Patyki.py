a,b,c=map(int, input().split())
if a==b==c:
    print(2)
elif 2 * max(a, b, c) ** 2 == a * a + b * b + c * c:
    print(1)
else:
    print(0)