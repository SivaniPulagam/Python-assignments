a=int(input('Enter a value for a:'))
b=int(input('Enter a value for b:'))
c=int(input('Enter a value for c:'))
d=int(input('Enter a value for d:'))
if a>b and a>c and a>d:
 print('a is big')
elif b>c and b>d:
 print('b is big')
elif c>d:
 print('c is big')
else:
 print('d is big')
