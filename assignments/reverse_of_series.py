n = int(input())
m = int(input())
c = n*m
for i in range(0, n):
    for j in range(0, m):
        print(c, end=' ')
        c-= 1
    print()
