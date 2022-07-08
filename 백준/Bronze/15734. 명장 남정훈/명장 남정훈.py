l, r, a = map(int, input().split())
lr = min(l, r)
ans = 2 * lr
l -= lr
r -= lr
if l:
    ans += 2 * min(l, a)
    a -= min(l, a)
elif r:
    ans += 2 * min(r, a)
    a -= min(r, a)
ans += (a // 2) * 2
print(ans)
