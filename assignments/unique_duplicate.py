n=int(input())
l=list(map(int,input().split()))
check=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            check=check+1
if check==0:
    print("Unique")
else:
    print("Duplicate")
