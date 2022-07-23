n = int(input())
ans = [0] * 10
w = 1
while n > 0:
    now = (n // 10) * 10 + 9
    for i in range(10):
        ans[i] += (n // 10 + 1) * w
    for i in range(10 - now + n, 10):
        ans[i] -= w
    for c in list(str(n)[:-1]):
        ans[int(c)] -= (now - n) * w
    ans[0] -= w
    n //= 10
    w *= 10
print(*ans)
