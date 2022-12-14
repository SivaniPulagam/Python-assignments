n = int(input())
lst = list(map(int, input().split()))
l = []
for i in range(0, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (lst[i] < lst[j]):
                l = lst[i]
                lst[i] = lst[j]
                lst[j] = l
for i in range(0,n):
    print(lst[i])
