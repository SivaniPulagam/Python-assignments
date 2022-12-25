def is_positive(n):
    if n > 0:
        return True


n = int(input())
if is_positive(n):
    print("Positive")
else:
    print("Negative")
