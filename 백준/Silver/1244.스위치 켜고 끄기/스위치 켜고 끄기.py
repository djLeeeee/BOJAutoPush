num = int(input())
switch = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    s, n = map(int, input().split())
    if s == 1:
        for i in range(n - 1, num, n):
            switch[i] = int(not switch[i])
    elif s == 2:
        switch[n - 1] = int(not switch[n - 1])
        if min(num - n, n - 1) == 1 and (switch[(n - 1) - 1] == switch[(n - 1) + 1]):
            switch[(n - 1) - 1] = int(not (switch[(n - 1) - 1]))
            switch[(n - 1) + 1] = int(not (switch[(n - 1) + 1]))
        else:
            for i in range(1, min(num - n + 1, n)):
                if switch[(n - 1) - i] == switch[(n - 1) + i]:
                    switch[(n - 1) - i] = int(not (switch[(n - 1) - i]))
                    switch[(n - 1) + i] = int(not (switch[(n - 1) + i]))
                else:
                    break

while switch:
    print(*switch[:20])
    switch = switch[20:]
