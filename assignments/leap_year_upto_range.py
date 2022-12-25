n = int(input())
m = int(input())
start = 0
for i in range(n, m + 1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        start = i
        break
while (start <= m):
    print(start, end=' ')
    start += 4
