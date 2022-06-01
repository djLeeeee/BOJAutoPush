from sys import stdin

input = stdin.readline

fb = [1, 2]
while fb[-1] < 10 ** 6:
    fb.append(fb[-1] + fb[-2])
n = int(input())
flag = False
for i in fb[::-1]:
    if i == n:
        if flag:
            print(i)
        else:
            print(-1)
        break
    elif i < n:
        n -= i
        flag = True