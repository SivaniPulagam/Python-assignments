n=int(input("Enter a number:"))
rev=0
temp=n
while(n>0):
    i=n%10
    rev=rev*10+i
    n=n//10
if(temp==rev):
    print("Given number is palindrome")
else:
    print("Given number is not a palindrome")




