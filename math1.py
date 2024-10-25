
import cmath
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=(b**2-4*a*c)
if (d>0):
   e=(-b+(d)**(1/2))/(2*a)
   g=(-b-(d)**1/2)/(2*a)
   print("the roots are realand distinct")
   print("Root1=",e)
   print("Root2=",g)
elif (d==0):
   e=(-b+(d)**(1/2))/(2*a)
   g=(-b-(d)**(1/2))/(2*a)
   print("the roots are real and equal")
   print("Root1=%.2f"%e)
   print("Root2=%.2f"%g)
else:
   e=(-b+cmath.sqrt(d))/(2*a)
   g=(-b-cmath.sqrt(d))/(2*a)
   print("the roots are imaginary")
   print("Root1=%.2f+%.2fj"%(e.real,e.imag))
   print("Root2=%.2f%.2fj"%(g.real,g.imag))
