def is_prime(n):
    if n==2: return True
    if n<=1 or (n%2==0): return False
    i = 3
    while(i*i<n+1):
        if n%i==0:
            return False
        i+=1
    return True

def factorial(n):
    fact = 1
    while n>1:
        fact = fact * n
        n-=1
    return fact
sum = 0
numbers = int(input())
for i in range(numbers):
    n = int(input())
    if is_prime(n) == False:
        sum += factorial(n)
print(sum)