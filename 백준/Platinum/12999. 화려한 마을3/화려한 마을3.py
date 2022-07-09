from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
querys = []
for i in range(m):
    s, e = map(int, input().split())
    querys.append((s - 1, e - 1, i))
sn = n ** 0.5
querys.sort(key=lambda x: (x[0] // sn, x[1]))
ans = [0] * m
cnt = defaultdict(int)
cnt_inv = defaultdict(int)
cnt_inv[0] = n
ps, pe, _ = querys[0]
for idx in range(ps, pe + 1):
    cnt_inv[cnt[arr[idx]]] -= 1
    cnt[arr[idx]] += 1
    cnt_inv[cnt[arr[idx]]] += 1
mx = max(cnt.values())
for s, e, i in querys:
    if ps < s:
        for idx in range(ps, s):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    elif s < ps:
        for idx in range(s, ps):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if cnt[arr[idx]] > mx:
                mx = cnt[arr[idx]]
    if pe < e:
        for idx in range(pe + 1, e + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if cnt[arr[idx]] > mx:
                mx = cnt[arr[idx]]
    elif e < pe:
        for idx in range(e + 1, pe + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    ps, pe = s, e
    ans[i] = str(mx)
print('\n'.join(ans))
