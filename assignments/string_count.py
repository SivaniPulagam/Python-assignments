s = input("Enter any string:")
count = 0
for i in range(0, len(s)):
    if (s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'z'):
        count = count + 1
print("Total number of characters in a string: " + str(count))
