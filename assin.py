#1 
x=int(input("given number"))
b=1
while(b<=x):
          if(b%3==0 and b%7==0):
                                print(b)
          b=b+1
print("end")
#2
n= int(input("enter number"))
sum=0
for m in range (1,n):
        if(m%2==0):
         sum=sum+m
print(sum)   #sum of even numbers 
for x in range(1,n):
                   if (x%2==0):
                                print(x)  #even numbers  
#3
k=1
d=int(input("enter num"))
while(k<=10):
       print(d,"*",k,"=",d*k)
       k=k+1# table of any number
 #4
for j in range(65,91):
                         print(chr(j),end='')#alphabets
#6
u=int(input("enter put"))
for x in range(1,u):
                   if (x%2!=0):
                                print(x)  #odd numbers
#5
a=int(input("enter number n "))
if(a<0):
       print("enter valid number")
elif(a==0):
       print("factorial of 0 is 1")
else:
     x=1
     for i in range(1,a+1):
         x=x*i
     print("factorial of {} is {}".format(a,x))#factorial of given number
#6
n=int(input("enter number"))
i=1
s=0
while(i<=n):
     if(n%i==0):
             
            s=s+i
     i=i+1
print(s)#sum of factors
#7
n=int(input("enter number"))
c=0
for i in range(1,n+1):
        if(n%i==0):
              c=c+1
if(c==2):
         print("it is aprime number ")
else:
     print("its not prime") #to find its prime or not 
#8
a=int(input("enter user number "))
x=str(a)
for i in x:
          print(i)
#9
n=int(input("enter yput num"))
x=str(n)
for i in range (1,n):
        sum=sum+pow(int(i)**3)
if(n==sum):
          print("its a armstang")
else:
     print("it is not an armstrong")#its an armstrong 
#10
n=int(input("enter number"))
sum=0
for x in range(1,n): 
          if n%x==0:
             sum=sum+x
if(n==sum):
         print(n,"is perfect number")
else:
     print("its not a perfect number")#perfect number 
#12
a=1
n=int(input("enter second num"))
for x in range(a,n+1):
          if x>1:
               for i in range(2,x):
                               if(x%i==0):
                                    break
               else:
                   print(x)#primr numbers upto n
#12





