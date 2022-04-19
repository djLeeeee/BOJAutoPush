from sys import stdin

input = map(int, stdin.read().split())

arr = [next(input) for _ in range(4)]
if arr[0] == arr[1] == arr[2] == arr[3]:
    print('Fish At Constant Depth')
elif arr[0] < arr[1] < arr[2] < arr[3]:
    print('Fish Rising')
elif arr[0] > arr[1] > arr[2] > arr[3]:
    print('Fish Diving')
else:
    print('No Fish')