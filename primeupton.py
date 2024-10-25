n=int(input("enter a number:"))
for i in range(1,n+1):
	c=0
	for f in range(1,i+1):
		if (i%f==0):
			c=c+1
if c==2:
	print(i)
   #while loop 
   num=2
while(n<=2):
        c=0
        i=2
        while(i<=num//2):
                      if(num//i==0):
                                c=c+1
                                break
                       i=i+1
        if(c==0 and num!=1):
                          print(num)
        num=num+1
