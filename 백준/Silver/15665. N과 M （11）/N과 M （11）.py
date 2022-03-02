def permutation(picked, idx):
    if len(picked) == idx:
        a = [nums[i] for i in picked]
        answer.add(tuple(a))
        return
    for i in range(n):
        permutation(picked + [i], idx)


n, m = map(int, input().split())
array = list(range(n))
nums = list(set(map(int, input().split())))
n = len(nums)
nums.sort()
answer = set()
permutation([], m)
answer = list(answer)
answer.sort()
for line in answer:
    print(*line)
