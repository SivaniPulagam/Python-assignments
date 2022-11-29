balance=10000
amount=int(input('Enter your amount'))
if amount < balance:
  d=balance-amount
  print('Credited amount:',amount)
  print('Main balance:',d)
  
else:
  print('in sufficient balance in your account')
