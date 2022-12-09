def get_nxt_val(n):
    total_sum =0
    while n>0:
        n, digit = divmod(n, 10)
        total_sum += digit ** 2
    return total_sum
n = int(input())
seen  = set()

while n !=1 and n not in seen:
    seen.add(n)
    n = get_nxt_val(n)
if n==1:
    print("Happy Number")
else:
    print("Not a Happy Number")