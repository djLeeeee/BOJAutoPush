ans = [0] * 26
t = input()
for c in t:
    ans[ord(c) - ord('a')] += 1
print(*ans)