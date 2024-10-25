L=[]
while True:
        print("a- to add element")
        print("p-to print the list")
        print("v-find the average of the list values")
        print("r-to remove an element")
        print("m-to find minimum")
        print("q-quit")

        op=str(input("Choose any option form above menue:"))
        y=0
        if  op=='a':
            x=int(input("Enter any element to add list:"))
            L.append(x)
        elif op=='p':
             print(L)
        elif op=='v':
             print("The average of list values is:",sum(L)/len(L))
        elif op=='r':
             k=int(input("enter element you want to remove:"))
             L.remove(k)
        elif op=='m':            
             print("The minimum vlaue in the list is ",min(L))
        elif op=='q':
             breakl
