from sys import stdin as s


def max_fix(target):
    n = len(target)
    pi = [0] * n
    idx = 0
    for i in range(1, n):
        while idx > 0 and target[idx] != target[i]:
            idx = pi[idx - 1]
        if target[idx] == target[i]:
            idx += 1
            pi[i] = idx
    return max(pi)


editor = s.readline().strip()
length = len(editor)
ans = 0
for j in range(length - 1):
    ans = max(ans, max_fix(editor[j:]))
print(ans)
