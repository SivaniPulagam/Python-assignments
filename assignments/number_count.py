s = input("Enter any string:")
count = 0
for i in range(0, len(s)):
    if (s[i] >= '0' and s[i] <='9'):
        count = count + 1
print("Total number of characters in a string: " + str(count))
