from sys import stdin as s

def check_fix(word):
    l = len(word)
    result = [0] * l
    i = 0
    for j in range(1, l):
        while word[i] != word[j] and i > 0:
            i = result[i - 1] 
        if word[i] == word[j]:
            i += 1
            result[j] = i
    return l - result[-1]

n = int(s.readline())
word = s.readline().strip()
print(check_fix(word))