from sys import stdin as s

while True:
    target = s.readline().strip()
    if target == '.':
        break
    n = len(target)
    pi = [0] * n
    idx = 0
    for i in range(1, n):
        while idx > 0 and target[idx] != target[i]:
            idx = pi[idx - 1]
        if target[idx] == target[i]:
            idx += 1
            pi[i] = idx
    if n % (n - pi[-1]) == 0:
        print(n // (n - pi[-1]))
    else:
        print(1)
