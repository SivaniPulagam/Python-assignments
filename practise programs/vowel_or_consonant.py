def is_vowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == '0' or ch == 'u' or \
        ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'


ch = input()
if is_vowel(ch):
    print("Vowel")
else:
    print("Consonant")
