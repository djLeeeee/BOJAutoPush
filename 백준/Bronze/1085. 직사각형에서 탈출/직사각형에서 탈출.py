a,b,c,d = map(int, input().split())
print(min(a, abs(a - c), b, abs(b - d)))