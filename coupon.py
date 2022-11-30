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
couponcode=input('Enter couponcode of the customer:')
if couponcode=="Diwali":
    if bill>=5000:
        dis=bill*10/100
    if bill>=3000:
        dis=bill*6/100
    if bill>=1000:
        dis=bill*4/100
    else:
        dis=0
if couponcode=="Christmas":
    if bill>=3000:
        dis=bill*20/100
    if bill>=2000:
        dis=bill*10/100
    if bill>=1000:
        dis=bill*5/100
    else:
        dis=0
    
print('customer phone number',cphno)
print('customer name:',cname)
print('Address:',address)
print('discount is:',dis)
print('bill is:',bill-dis)
