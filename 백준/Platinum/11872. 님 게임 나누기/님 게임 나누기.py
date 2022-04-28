n = int(input())
state = 0
for num in map(int, input().split()):
    if num % 4 == 0:
        state ^= num - 1
    elif num % 4 == 3:
        state ^= num + 1
    else:
        state ^= num
print('koosaga' if state else 'cubelover')
