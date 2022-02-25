n = int(input())
if n <= 3:
    print(n)
else:
    start = 1
    ans = 0
    div = 2
    while start <= n:
        ans += (n - start) // div + 1
        start = start * 4 + 6
        div *= 4
    two = 2
    while two <= n:
        ans += 1
        two = two * 4 + 6
    print(ans)
