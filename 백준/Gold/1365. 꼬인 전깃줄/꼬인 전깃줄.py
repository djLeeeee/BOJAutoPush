from sys import stdin as s

input = s.readline


def div_find(array, target):
    start = 0
    end = len(array) - 1
    ans = end
    while start <= end:
        middle = (start + end) // 2
        if array[middle] < target:
            start = middle + 1
        else:
            ans = middle
            end = middle - 1
    return ans


n = int(input())
lines = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
stack = [lines[0]]
length = 1
for line in lines[1:]:
    if stack[-1] < line:
        stack.append(line)
        length += 1
    else:
        idx = div_find(stack, line)
        stack[idx] = line
print(n - length)
