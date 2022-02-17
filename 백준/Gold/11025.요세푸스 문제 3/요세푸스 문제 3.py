from sys import stdin as s

n, m = map(int, s.readline().split())
result = 0
for i in range(1, n + 1):
    result = (result + m) % i
print(result + 1)