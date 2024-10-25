n=int(input("enter n times"))
i=0
k=[]
while i<n:
           x=int(input("enter element"))
           k.append(x)
           i=i+1
print(k)
n=int(input("enter n times"))
i=0
m=[]
while i<n:
           x=int(input("enter element"))
           m.append(x)
           i=i+1
print(m)
c=0
for i in k :
            if i in m:
                      c=c+1
if c!=1:
             print("true")
else:
      print("false")
for i in range(len(k)):
   a=k[i]
for i in range(len(m)):
     b=m[i]
if a==b:
       print("true")
      
