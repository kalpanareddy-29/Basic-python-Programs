c=2244
sum=0
while(c>0):
       d=c%10
       sum=sum+d
       c=c//10
print("the sum of the digits",sum)#sum of digits in a number 
num=2244
rev=0
while(num>0):
           d=num%10
           rev=(rev*10)+d
           num=num//10
print("the reverse number is :",rev)
#reverse the digits of a number 
a=int(input("enter amount"))
n=[5000,2000,1000,500,100,50,20,10,5,2,1]
t={}
for i in n:
         x=a%i
         t[i]=x
         a=a-(i*x)
print(t)
