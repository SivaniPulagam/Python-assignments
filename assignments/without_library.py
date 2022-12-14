l = []
n = int(input())
l = list(map(int, input().split()))
min = l[0]
max = l[-1]
for i in range(1, n):
    if l[i] < min:
        min = l[i]
for j in range(1, n):
    if l[j] > max:
        max = l[j]

print(min)
print(max)
