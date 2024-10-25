for i in range(1,200):
       x=i
       n=len(str(i))
       sum=0
       i=str(i)
       for c in i:
            sum=sum+int(c)**n
       if(sum==x):
          print(x)#angstong number b/w 2 numbers
          
       
