p=int(input("Principal amount:"))
t=int(input("Time period:"))
r=float(input("Rate of interest:"))
si=(p*t*r)/100
emi=(si+p)/t*12
print("SI is :",si)
print("EMI is:",emi)

