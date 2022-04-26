from sys import stdin
from itertools import combinations

input = stdin.readline

L, C = map(int, input().split())
char = input().strip().split()
char.sort()
orders = list(combinations(range(C), L))
for order in orders:
    ans = ''
    vowel = 0
    for idx in order:
        ans += char[idx]
        if char[idx] in 'aeiou':
            vowel += 1
    if 0 < vowel < L - 1:
        print(ans)
