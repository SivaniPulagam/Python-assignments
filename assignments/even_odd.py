n=int(input())
l=list(map(int,input().split()))
i = 0
for j in range(n):
    if l[j]%2==0:
        l[i],l[j] = l[j],l[i]
        i+=1
print(l)