# 12728 n 제곱 계산


from sys import stdin as s

input = s.readline

n = int(input())


def multiple(first, second=None):
    if not second:
        second = first
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            ans[i][j] += first[i][0] * second[0][j]
            ans[i][j] += first[i][1] * second[1][j]
    return ans


for t in range(1, n + 1):
    k = int(input())
    k -= 1
    k %= 1000
    x = [[1, 0], [0, 1]]
    matrix = [[6, -4], [1, 0]]
    while k > 0:
        if k & 1:
            x = multiple(x, matrix)
        k >>= 1
        matrix = multiple(matrix)
    print(f'Case #{t}: ', end='')
    answer = int(x[0][0] * 6 + x[0][1] * 2) % 1000 - 1
    if answer == -1:
        answer = 999
    answer = str(answer)
    while len(answer) < 3:
        answer = '0' + answer
    print(answer)
