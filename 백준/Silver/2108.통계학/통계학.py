import sys

n = int(sys.stdin.readline())

N = 4000

a = [0 for _ in range(2 * N + 1)]
min = N + 1
max = -N - 1
for _ in range(n):
    num = int(sys.stdin.readline())
    a[num + N] += 1
    if min > num:
        min = num
    if max < num:
        max = num

M = 1
maximum = []
sum = 0
order = 0
for i, j in enumerate(a):
    sum += (i - N) * j
    if order <= n // 2:
        order += j
        middle = i - N
    if j > M:
        maximum = [i - N]
        M = j
    elif j == M:
        if len(maximum) <= 1:
            maximum.append(i - N)

print(round(sum / n))
print(middle)
print(maximum[-1])
print(max - min)
