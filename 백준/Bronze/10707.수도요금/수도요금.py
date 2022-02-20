a= int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a * e < b + max(e - c, 0) * d:
    print(a * e)
else:
    print(b + max(e - c, 0) * d)