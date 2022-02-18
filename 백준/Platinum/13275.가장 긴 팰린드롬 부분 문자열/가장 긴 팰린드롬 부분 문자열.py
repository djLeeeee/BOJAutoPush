def max_palindrome(my_lst):
    length = 0
    for i in range(len(my_lst)):
        if my_lst[i - length: i + 1] == my_lst[i - length: i + 1][::-1]:
            length += 1
        elif i > length:
            if my_lst[i - length - 1: i + 1] == my_lst[i - length - 1: i + 1][::-1]:
                length += 2
    return length


print(max_palindrome(input()))