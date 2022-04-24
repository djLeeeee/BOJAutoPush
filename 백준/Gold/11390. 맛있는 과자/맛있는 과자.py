from sys import stdin
from math import log

input = stdin.readline

a, b, n, k = map(int, input().split())
f = [1] * (n + 1)
for i in range(2, n + 1):
    f[i] = f[i - 1] * i
total = 1
m = 0
while total < k:
    m += 1
    total += f[n] // (f[m] * f[n - m])
a, b = min(a, b), max(a, b)
aa = a * a
bb = b * b
ans = log(a) + log(b) - log(2) + m * log(aa / (aa + bb)) + (n - m) * log(bb / (aa + bb))
print(ans)
