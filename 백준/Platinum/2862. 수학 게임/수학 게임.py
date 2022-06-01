from sys import stdin

input = stdin.readline

fb = [1, 2]
while fb[-1] < 10 ** 15:
    fb.append(fb[-1] + fb[-2])
n = int(input())
for i in fb[::-1]:
    if i == n:
        print(i)
        break
    elif i < n:
        n -= i