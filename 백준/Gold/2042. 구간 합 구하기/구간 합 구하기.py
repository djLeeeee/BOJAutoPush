from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
tree = [0] * (2 * n)
for i in range(n):
    tree[n + i] = int(input())
for i in range(n - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]
for _ in range(m + k):
    query = tuple(map(int, input().split()))
    if query[0] == 1: 
        idx = query[1] + n - 1
        tree[idx] = query[2]
        idx //= 2
        while idx >= 1:
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
            idx //= 2
    elif query[0] == 2:
        result = 0
        left = query[1] + n - 1
        right = query[2] + n - 1
        while left <= right:
            if left % 2:
                result += tree[left]
                left += 1
            if not right % 2:
                result += tree[right]
                right -= 1
            left //= 2
            right //= 2
        print(result)