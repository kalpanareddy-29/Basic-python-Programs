n=int(input("enter n times"))
i=0
k=[]
while i<n:
           x=int(input("enter element"))
           k.append(x)
           i=i+1
print(k)

for i in k:
          if i%2==0:
               k.remove(i)
print(k)
q112
