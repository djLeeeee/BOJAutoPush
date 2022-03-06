def work(nums):
    sec = 0
    for i in range(3):
        sec += (nums[i + 3] - nums[i]) * trans[i]
    ans = []
    for j in range(3):
        ans.append(sec // trans[j])
        sec %= trans[j]
    return ans


trans = [3600, 60, 1]
for _ in range(3):
    print(*work(list(map(int, input().split()))))
