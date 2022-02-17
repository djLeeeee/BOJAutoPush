from sys import stdin as s


def power(a, b):
    result = 1
    while b:
        if b & 1:
            result *= a
            result %= 1000000007
        a = a * a
        a %= 1000000007
        b >>= 1
    return result


n = int(s.readline())
for _ in range(n):
    N = int(s.readline())
    if N == 1:
        print(1)
    else:
        print(power(2, N - 2) % 1000000007)
