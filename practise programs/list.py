boys = []
girls = []
n = int(input("Enter no of boys"))
for i in range(n):
    x = input("Enter boy name: ")
    boys.append(x)

m = int(input("Enter no of girls:"))
for i in range(m):
    x = input("Enter girl name:")
    girls.append(x)
print(boys)
print(girls)
boys.insert(2, 'mahesh')
print(boys)
print(boys + girls)
print('************************************************')
girls.extend(boys)
print(girls)
