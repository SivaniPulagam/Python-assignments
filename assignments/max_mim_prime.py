import math
def is_prime(n):
    if n == 2: return 1
    if n <= 1 or (n % 2 == 0): return 0
    i = 3
    while (i < int(math.sqrt(n + 1))):
        if n % i == 0:
            return 0
        i += 1
    return 1

n = int(input())
l = [int(i) for i in input().split()]
max_prime, min_prime = -1, 9999999999999

for i in l:
    if is_prime(i):
        max_prime = max(max_prime, i)
        min_prime = min(min_prime, i)
print(max_prime, min_prime)