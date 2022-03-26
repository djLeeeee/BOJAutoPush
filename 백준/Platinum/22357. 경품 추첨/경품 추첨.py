from sys import stdin

input = stdin.readline


def prime_list(cnt):
    result = set()
    check = [True] * 3000
    pointer = 3
    while len(result) < cnt:
        if check[pointer]:
            if pointer > 2000:
                result.add(pointer)
            for i in range(pointer, 3000, 2 * pointer):
                check[i] = False
        pointer += 2
    return result


n, m = map(int, input().split())
subs = prime_list(n)
for sub in subs:
    ans = []
    s = 1
    for _ in range(m):
        ans.append(s)
        s += sub
    print(*ans)
