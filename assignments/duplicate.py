n = int(input())
l = list(map(int, input().split()))
m = []
for i in l:
    if i not in m:
        m.append(i)
print(m)
