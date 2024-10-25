n=int(input("enter num"))

for i in range(1,n+1):
              if(n%i==0):
                      c=0
                      for f in range(1,i+1):
                                       if(i%f==0):
                                             c+=1
                      if(c==2):
                               print(i)
