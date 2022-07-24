n, k = map(int, input().split())
entry = []
bit = 1
while n >= bit:
    if n & bit:
        entry.append(bit)
    bit *= 2
ans = 0
entry = entry[::-1]
while len(entry) > k:
    now = entry.pop()
    ans += now
    while entry and entry[-1] == 2 * now:
        entry.pop()
        now *= 2
    entry.append(now * 2)
print(ans)
