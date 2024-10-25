for i in range(1,101):
       x=i
       n=len(str(i))
       sum=0
       i=str(i)
       for x in i:
            sum=sum+int(x)**n
       if(sum==x):
          print(x)
