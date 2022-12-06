n=int(input("Enter a number:"))
sum=0
temp=n
while(n>0):
    i=n%10
    sum=sum+i**3
    n=n//10
if(temp==sum):
    print("Given number is amstrong number")
else:
    print("Given number is not a amstrong number")
