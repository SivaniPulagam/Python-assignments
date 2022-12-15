n=int(input())
l=list(map(int,input().split()))
# pos=[]
# neg=[]
# for i in range(0,n):
#     if l[i]>=0:
#         pos.append(l[i])
#     else:
#         neg.append(l[i])
# l=pos+neg
# print(l,end=' ')

i = 0
for j in range(n):
    if l[j]>=0:
            l[i],l[j] = l[j],l[i]
            i+=1
print(l)