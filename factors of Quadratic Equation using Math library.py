import math
a=int(input("enter numeric value for a:"))
b=int(input("enter numeric value for b:"))
c=int(input("enter numeric value for c:"))
d=pow(b,2)-(4*a*c)
e=(-b+math.sqrt(d))/2*a
f=(-b-math.sqrt(d))/2*a
print("factor1:",e)
print("factor2:",f)
