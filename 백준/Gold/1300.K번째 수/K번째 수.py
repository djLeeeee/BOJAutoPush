from sys import stdin as s

n = int(s.readline())
k = int(s.readline())
start = 1
end = k
while start <= end:
    middle = (start + end) // 2
    idx = 0
    for i in range(1, n + 1):
        idx += min(n, middle // i)
    if idx >= k:
        end = middle - 1
        ans = middle
    elif idx < k:
        start = middle + 1
print(ans)
