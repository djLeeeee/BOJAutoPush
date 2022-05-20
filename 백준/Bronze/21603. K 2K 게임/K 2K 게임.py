n, k = map(int, input().split())
x, y = k % 10, (2 * k) % 10
ans = [i for i in range(1, n + 1) if i % 10 != x and i % 10 != y]
print(len(ans))
print(*ans)