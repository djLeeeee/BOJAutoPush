n = int(input())
arr = list(map(int, input().split()))
grundy = 0
for num in arr:
    if num % 2:
        grundy ^= num // 2 + 1
    else:
        grundy ^= num // 2 - 1
print('koosaga' if grundy else 'cubelover')