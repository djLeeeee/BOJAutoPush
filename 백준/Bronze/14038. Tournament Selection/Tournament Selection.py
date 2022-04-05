cnt = 1
for _ in range(6):
    if input() == 'W':
        cnt += 1
cnt //= 2
print(4 - cnt if cnt else -1)
