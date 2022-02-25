from sys import stdin as s

input = s.readline


def search(array, target):
    start = 0
    end = len(array)
    while start < end:
        middle = (start + end) // 2
        if array[middle] <= target:
            start = middle + 1
        else:
            end = middle
    return end


n, c = map(int, input().split())
mass = list(map(int, input().split()))
sum_left = []
m = n - n // 2
n //= 2
for i in range(1 << n):
    s = 0
    for j in range(n):
        if i >> j & 1:
            s += mass[j]
    sum_left.append(s)
sum_left.sort()
ans = 0
for p in range(1 << m):
    t = 0
    for q in range(m):
        if p >> q & 1:
            t += mass[n + q]
    ans += search(sum_left, c - t)
print(ans)
