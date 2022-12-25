def is_even(n):
    while(n!=0):
        return n%2==0

n=int(input("Enter a number:"))
if is_even(n):
    print("Even")
else:
    print("Odd")