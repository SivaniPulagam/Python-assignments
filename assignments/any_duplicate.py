def duplicate(l, n, k):
    m = []
    for i in range(n):
        if l[i] in m:
            return True
        m.append(l[i])
        if (i >= k):
            m.remove(l[i - k])
    return False


m=int(input())
l =list(map(int,input().split()))
n = len(l)
if (duplicate(l, n, 3)):
    print("Yes")
else:
    print("No")