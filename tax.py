empno=int(input('Enter empno:'))
empname=input('Enter empname:')
empdesig=input('Enter empdesig')
basicsalary=int(input('Enter basic salary of an emp:'))
da=int(input('Enter daily allowance of an emp:'))
ta=int(input('Enter travelling allowance of an emp:'))
hra=int(input('Enter house rental allowance of an emp:'))
netsalary=basicsalary+da+ta+hra
print(netsalary)
if netsalary>1000000:
    tax=netsalary*10/100
if netsalary>50000:
    tax=netsalary*7/100
if netsalary>40000:
    tax=netsalary*4/100
if netsalary>20000:
    tax=netsalary*2/100
if netsalary<20000:
    tax=0
print('Tax is:',tax)
