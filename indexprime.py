n=int(input("enter n times"))
i=0
k=[]
while i<n:
           x=int(input("enter element"))
           k.append(x)
           i=i+1
print(k)
m=len(k)
c=0
for i in range(m):
                   for y in range(1,i+1):
                           if y>1:
                               for z in range(2,y):
                                   if y%z==0:
                                           break
                               else:
                                    print(y)
k.remove(k[i])
print(k)
                         
                                    
             
