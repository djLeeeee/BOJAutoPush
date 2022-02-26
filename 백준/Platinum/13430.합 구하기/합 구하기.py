k, n = map(int, input().split())
n, k = n + k, min(k + 1, n - 1)
div = 1000000007
a = b = 1
for i in range(n, n - k, -1):
    a = (a * i) % div
for i in range(1, k + 1):
    b = (b * i) % div
print((a * pow(b, div - 2, div)) % div)
