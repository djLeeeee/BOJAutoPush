from sys import stdin

input = stdin.readline

s = [4, 8, 20, 24, 28]
for _ in range(int(input())):
    x = int(input())
    rx = x % 34
    print('Platina' if x == 14 or x == 34 or rx in s else 'Yuto')
