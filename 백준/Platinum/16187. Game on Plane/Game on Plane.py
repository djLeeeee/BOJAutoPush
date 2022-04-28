from sys import stdin

input = stdin.readline

grundy = [0] * 5001
grundy[2] = 1
for num in range(3, 5001):
    sub_grundy = set()
    remain = num - 2
    for left in range(remain // 2 + 1):
        right = remain - left
        sub_grundy.add(grundy[left] ^ grundy[right])
    for gn in range(num + 1):
        if gn not in sub_grundy:
            grundy[num] = gn
            break
for _ in range(int(input())):
    print('First' if grundy[int(input())] else 'Second')