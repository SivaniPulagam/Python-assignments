''''
def is_even(n):
    for i in range(1,n,2):
        print(i)

n=int(input("Enter a number:"))
is_even(n)
'''''


def is_even(n):
    i=0
    while (i<n):
        if i%2==0:
            print(i)
        i=i+1

n = int(input("Enter a number:"))
is_even(n)
