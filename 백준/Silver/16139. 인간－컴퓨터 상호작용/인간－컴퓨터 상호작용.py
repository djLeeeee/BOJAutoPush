from sys import stdin

input = stdin.readline

word = input().strip()
cnt = [[0] * 26 for _ in range(len(word) + 1)]
for i in range(len(word)):
    cnt[i] = cnt[i - 1][:]
    cnt[i][ord(word[i]) - ord('a')] += 1
for _ in range(int(input())):
    t, s, e = input().split()
    t = ord(t) - ord('a')
    print(cnt[int(e)][t] - cnt[int(s) - 1][t])