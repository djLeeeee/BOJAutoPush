y, m, d = map(int, input().split())
ny, nm, nd = map(int, input().split())
if m < nm:
    print(ny - y)
elif m == nm and d <= nd:
    print(ny - y)
else:
    print(ny - y - 1)
print(ny - y + 1)
print(ny - y)