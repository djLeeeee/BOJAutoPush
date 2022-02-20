from sys import stdin as s

n, k = map(int, s.readline().split())
if n >= k:
    print(n - k)
    print(*list(range(n, k - 1, -1)))
else:
    visited = [0] * 100001
    starts = [k]
    ans = 1
    visited[k] = ans
    while not visited[n]:
        ans += 1
        new_starts = []
        for start in starts:
            if start % 2 == 0 and not visited[start // 2]:
                visited[start // 2] = ans
                new_starts.append(start // 2)
            if start + 1 <= 100000 and not visited[start + 1]:
                visited[start + 1] = ans
                new_starts.append(start + 1)
            if not visited[start - 1]:
                visited[start - 1] = ans
                new_starts.append(start - 1)
        starts = new_starts
    print(ans - 1)
    result = [0] * ans
    result[0] = n
    for i in range(1, ans):
        ans -= 1
        if 2 * n < 100001 and visited[2 * n] == ans:
            n = 2 * n
        elif n + 1 < 100001 and visited[n + 1] == ans:
            n += 1
        else:
            n -= 1
        result[i] = n
    print(*result)
