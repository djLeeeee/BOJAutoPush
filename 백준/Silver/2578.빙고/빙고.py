from sys import stdin as s

def check_bingo(my_list):
    result = 0
    for i in range(5):
        if sum(my_list[5 * i:5 * i + 5]) == 0:
            result += 1
        if sum(my_list[i::5]) == 0:
            result += 1
    if sum(my_list[0::6]) == 0:
        result += 1
    if sum(my_list[4:21:4]) == 0:
        result += 1
    return result

chulsu = [ ]
for _ in range(5):
    chulsu += list(map(int, s.readline().split()))

jinhang = [ ]
for _ in range(5):
    jinhang += list(map(int, s.readline().split()))

for i in range(25):
    a = chulsu.index(jinhang[i])
    chulsu[a] = 0
    if check_bingo(chulsu) >= 3:
        break
print(i + 1)