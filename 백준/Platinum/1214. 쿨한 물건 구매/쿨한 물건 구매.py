from sys import stdin

input = stdin.readline

d, p, q = map(int, input().split())
if p == q:
    if d % p:
        print((d // p + 1) * p)
    else:
        print(d)
elif d % p and d % q:
    p, q = min(p, q), max(p, q)
    ans = (d // q + 1) * q
    for i in range(d // q, max(-1, d // q - p), -1):
        remain = d - q * i
        if remain % p == 0:
            ans = d
            break
        else:
            if q * i + (remain // p + 1) * p < ans:
                ans = q * i + (remain // p + 1) * p
    print(ans)
else:
    print(d)
