def is_prime(elem):
    if elem == 2:
        return 1
    if elem <= 1 or (elem % 2 == 0):
        return 0
    num = 3
    while num *num <elem+1:
        if elem % num == 0:
            return 0
        num += 1
    return 1
def primeSum(l, r):
    sum = 0
    for i in range(l,r+1):
        primeSum = is_prime(i)
        if (primeSum):
            sum += i
    return sum

l=int(input())
r=int(input())
print(primeSum(l,r))