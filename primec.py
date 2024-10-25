n=int(input("enter number"))
c=0
for i in range(1,n+1):
        if(n%i==0):
                 c=c+1
if(c==2):
         print("it is aprime number ",n)
else:
     print("its not prime",n)
     #while
k=int(input("enter number"))
c=0
m=1
while(m<=k):
           if(k%m==0):
                  c=c+1
           m=m+1
if(c==2):
        print("its a prime")
else:
    print("its not a prime")

    

