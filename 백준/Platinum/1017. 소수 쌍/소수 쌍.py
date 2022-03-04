from sys import stdin as s
from sys import setrecursionlimit as st

input = s.readline
st(10 ** 4)


def prime_list():
    checked = [False] * 2000
    result = set()
    for check in range(2, 2000):
        if checked[check]:
            continue
        result.add(check)
        time = 2
        while time * check < 2000:
            checked[time * check] = True
            time += 1
    return result


def dfs(start):
    for adj in graph[start]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == -1 or dfs(match[adj]):
            match[adj] = start
            return True
    return False


n = int(input())
nums = list(map(int, input().split()))
graph = [[] for _ in range(n)]
primes = prime_list()
for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] + nums[j] in primes:
            graph[i].append(j)
            graph[j].append(i)
ans = []
for num in graph[0]:
    match = [-1] * n
    match[num] = 0
    match[0] = num
    for k in range(1, n):
        visited = [False] * n
        visited[0] = True
        visited[num] = True
        dfs(k)
    if sum([1 for d in match if d >= 0]) == n:
        ans.append(nums[num])
if ans:
    ans.sort()
    print(*ans)
else:
    print('-1')
