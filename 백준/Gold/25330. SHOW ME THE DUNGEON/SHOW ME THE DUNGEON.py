from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
atk = list(map(int, input().split()))
per = list(map(int, input().split()))
ans = 0
now = [(0, 0, 0, 0)]
while now:
    new = []
    for checker, damage, pre, saved in now:
        for bit in range(n):
            if not (1 << bit) & checker:
                idx = checker + (1 << bit)
                now_pre = pre + atk[bit]
                if damage + now_pre <= k:
                    now_saved = saved + per[bit]
                    new.append((idx, damage + now_pre, now_pre, now_saved))
                    if now_saved > ans:
                        ans = now_saved
    now = new
print(ans)