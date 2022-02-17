from sys import stdin as s

while True:
    a = s.readline()
    if a == '0\n':
        break
    array = list(map(int, a.split()))
    n = array[0]
    array = [0] + array[1:] + [0]
    remain = [0]
    max1 = [0] * (n + 1)
    for i in range(1, n + 2):
        while remain and array[remain[-1]] > array[i]:
            now = remain.pop()
            max1[now] = array[now] * (i - now)
        remain.append(i)
    array.reverse()
    remain = [0]
    max2 = [0] * (n + 1)
    for i in range(1, n + 2):
        while remain and array[remain[-1]] > array[i]:
            now = remain.pop()
            max2[now] = array[now] * (i - now)
        remain.append(i)
    M = 0
    for i in range(1, n + 1):
        M = max(M, max1[i] + max2[-i] - array[-i - 1])
    print(M)
