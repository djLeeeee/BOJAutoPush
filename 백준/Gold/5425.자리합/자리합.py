# 5425 자리합
from sys import stdin as s

my_sum = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 0]


def sum_digit(num):
    if num < 10:
        return my_sum[num]
    ans = 0
    front = sum([int(i) for i in str(num)])
    remain = num % 10
    num //= 10
    front -= remain
    return num * 45 + 10 * sum_digit(num) + my_sum[remain] - front * (9 - remain)


for _ in range(int(s.readline())):
    a, b = map(int, s.readline().split())
    print(sum_digit(b) - sum_digit(a - 1))
