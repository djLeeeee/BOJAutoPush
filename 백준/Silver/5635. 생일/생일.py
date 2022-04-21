arr = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    arr.append((int(y), int(m), int(d), name))
arr.sort()
print(arr[-1][-1])
print(arr[0][-1])