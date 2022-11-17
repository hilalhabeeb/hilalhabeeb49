n = int(input("enter the size:"))
a=[]
print("enter the elements:")
for i in range(0,n):
    i=int(input())
    a.append(i)
    if(i%2==0):


        a.remove(i)
print("list after removing even no:",a)