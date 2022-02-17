from sys import stdin as s

n = int(s.readline())
switch = [int(i) for i in s.readline().split()]
b = int(s.readline())

for _ in range(b):
    gender, num = map(int, s.readline().split())
    if gender == 1:
        x = num
        while num <= n:
            switch[num - 1] = 1 - switch[num - 1]
            num += x
    else:
        i = 0
        while switch[num - i - 1] == switch[num + i - 1]:
            i += 1
            if num - i - 1 < 0 or num + i - 1 > n - 1:
                break
        for j in range(num - i, num + i - 1):
            switch[j] = 1 - switch[j]

for i in range(n):
    if (i + 1) % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end = ' ')