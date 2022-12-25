def perfect_number(n):
    i=1
    s=0
    while(i<n):
        if(n%i==0):
            s+=i
        i+=1
    if s==n:
        return 1

n=int(input())
if perfect_number(n):
    print("Perfect number")
else:
    print("Not a perfect number")
