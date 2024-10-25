c=2244
sum=0
while(c>0):
       d=c%10
       sum=sum+d
       c=c//10
print("the sum of the digits",sum)
n=input("enter digitd")
s=0
for x in n:
       s=s+int(x)
print(s) #sum of digits 
n=int(input("enter" ))
s=0
while (n>0):
           d=n%10
           s=s+1
           n=n//10
print(s)
n=input()
m=0
for i  in n:
          m=m+1
print(m)#number of digits of in a number 
m=int(input("enter number "))
a=1
while(m>0):
          d=m%10
          a=a*d
          m=m//10
print(a)
b=input("enter number")
f=1
for x in b:
           f=f*int(x)
print(f)#product of digits in a number 

