def leapyear(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    else:
        return False


n = int(input("Enter year:"))
if (leapyear(n)):
    print("Yes It is a leap year")
else:
    print("No It's not a leap year")
