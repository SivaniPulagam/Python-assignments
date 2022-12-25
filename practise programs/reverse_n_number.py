'''
def is_number(n):
    while (n >= 0):
        print(n)
        n -= 1


n = int(input("Enter a number:"))
is_number(n)
'''''


def is_number(n):
    i=n
    for i in range(n,-1,-1):
        print(i)

n = int(input("Enter a number:"))
is_number(n)
