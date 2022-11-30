dairymilk=180
maggie=500
bread=30
jam=50
thumsup=90
cphno=int(input('Enter customer phone number:'))
cname=input('Enter customer name:')
address=input('Enter customer address:')
dq=int(input('no of dairymilks:'))
mq=int(input('no of maggie packets:'))
bq=int(input('no of bread packets:'))
jq=int(input('no of jam bottles:'))
tq=int(input('no of thumsup :'))
bill=(dq*dairymilk)+(mq*maggie)+(bq*bread)+(jq*jam)+(tq*thumsup)
print(bill)
if bill>3000:
 tax=bill*5/100
elif bill>2000:
 tax=bill*7/100
elif bill>500:
 tax=bill*15/100
else:
 tax=100
bill=tax+bill
print(cphno)
print(cname)
print(address)
print(bill)
