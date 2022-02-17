from sys import stdin as s
from collections import deque

t = int(s.readline())

for _ in range(t):
    n, stick, nth_fall = map(int, s.readline().split()) 
    ideal = []
    real = deque()
    for _ in range(n):
        position, id = map(int, s.readline().split())
        real.append([position, id])
        if id > 0:
            ideal.append([stick - position, 1])
        else:
            ideal.append([position, -1])
    ideal.sort()
    ans = [ ]
    i = 0
    while i < nth_fall:
        if i + 1 < n:
            left = real[0]
            right = real[-1]
            if ideal[i][0] == ideal[i + 1][0]:
                if left[1] < right[1]:
                    ans.append(left[1])
                    real.popleft()
                    ans.append(right[1])
                    real.pop()
                    i += 1
                else:
                    ans.append(right[1])
                    real.pop()
                    ans.append(left[1])
                    real.popleft()
                    i += 1
            else:
                if ideal[i][1] > 0:
                    ans.append(right[1])
                    real.pop()
                else:
                    ans.append(left[1])
                    real.popleft()
        else:
            ans.append(real[0][1])
        i += 1
    print(ans[nth_fall - 1])