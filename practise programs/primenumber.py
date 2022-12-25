def is_prime(n):
    if n == 2: return 1
    if n <= 1 or (n % 2 == 0): return 0
    i = 3
    while (i * i < n + 1):
        if n % i == 0:
            return 0
        i += 1
    return 1


n = int(input())

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")





