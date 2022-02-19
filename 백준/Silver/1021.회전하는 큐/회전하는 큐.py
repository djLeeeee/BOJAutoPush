from sys import stdin as s
from collections import deque

n, m = map(int, s.readline().split())
deck = deque(range(1, n + 1))
ans = 0
for order in map(int, s.readline().split()):
    moved = 0
    while deck[0] != order:
        deck.append(deck.popleft())
        moved += 1
    deck.popleft()
    if moved < n / 2:
        ans += moved
    else:
        ans += (n - moved)
    n -= 1
print(ans)
