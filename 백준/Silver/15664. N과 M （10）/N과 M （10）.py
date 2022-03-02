def permutation(picked, idx):
    if len(picked) == idx + 1:
        a = [nums[i] for i in picked[1:]]
        answer.add(tuple(a))
        return
    for i in range(picked[-1] + 1, n):
        permutation(picked + [i], idx)


n, m = map(int, input().split())
array = list(range(n))
nums = list(map(int, input().split()))
nums.sort()
answer = set()
permutation([-1], m)
answer = list(answer)
answer.sort()
for line in answer:
    print(*line)
