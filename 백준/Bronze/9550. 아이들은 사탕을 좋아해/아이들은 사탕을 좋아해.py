for _ in range(int(input())):
    _,m = map(int,input().split())
    print(sum([a//m for a in map(int,input().split())]))