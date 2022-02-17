from sys import stdin as s

n, m, k = map(int, s.readline().split())

if n + 1 < m + k or n > m * k:
    print(-1)
else:    
    ans = list(range(k, 0, -1))
    if m != 1:
        length = (n - k) // (m - 1)
        remain = (n - k) % (m - 1)
        for i in range(m - 1 - remain):
            ans.extend(list(range(k + length, k, -1)))
            k += length
        length += 1
        for j in range(remain):
            ans.extend(list(range(k + length, k, -1)))
            k += length
    print(*ans) 