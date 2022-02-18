from collections import deque

n, k = map(int, input().split())
result = []
person = deque(range(1, n + 1))

while person:
    if n - 1 <= k:
        result.append(person.pop())
        n -= 1
        k -= n
    else:
        result.append(person.popleft())
        n -= 1
print(*result)