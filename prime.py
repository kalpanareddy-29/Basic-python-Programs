b=int(input("enter second num"))
for x in range(1,b+1):
          if x>1:
               for i in range(2,x):
                               if(x%i==0):
                                    break
               else:
                   print(x)
n=int(input("enter number "))
for m in range(1,n+1):
            if m>1:
                for k in range(2,m):
                       if(m%k==0):
                           break
                else:
                            print(m)   
