n = int(input("Enter the number of terms: "))
a = 0
b = 1
s = 0
print(a, b)
for x in range(2, n):
    c = a + b
    s+=c
    print(c)
    a = b
    b = c
print()
print("Sum of fibonacci series:",s)

