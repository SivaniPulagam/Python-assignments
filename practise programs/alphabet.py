def is_alphabet(n):
    return n >= 'a' and n <= 'z' or  n >= 'A' and n <= 'Z'



n = input()
if is_alphabet(n):
    print("Alphabet")
else:
    print("Not a Alphabet")
