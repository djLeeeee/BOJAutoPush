a, b, c = map(int, input().split())
ans = a * b * c
for i in [a, b, c]:
    if i % 2 == 0:
        ans //= i
if ans == 1:
    if a == 1 or b == 1 or c == 1:
        print(1)
    else:
        print(a * b * c)
else:
    print(ans)