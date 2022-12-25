def sum_of_number(n):
    s = 0
    while (n!= 0):
        r = n % 10
        s = s + (r * r)
        n //= 10
    return s


n = int(input())
while (n > 9):
    n = sum_of_number(n)
if n == 1 or n == 7:
    print("Happy number")
else:
    print("Not a happy number")
