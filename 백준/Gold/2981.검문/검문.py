from sys import stdin as s


def gcd(a, b):
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    return gcd(min(a, b), max(a, b) - min(a, b))


n = int(s.readline())
array = [int(s.readline()) for _ in range(n)]
array.sort()
sub = [array[i + 1] - array[i] for i in range(n - 1)]
answer = sub[0]
for j in range(n - 2):
    answer = gcd(answer, sub[-j - 1])
for k in range(2, answer // 2 + 1):
    if answer % k == 0:
        print(f'{k}', end=' ')
print(answer)
