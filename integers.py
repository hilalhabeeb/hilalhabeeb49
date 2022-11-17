l1=[]
n=int(input("enter number of elements:"))
for i in range(0,n):
    i=int(input())
    l1.append(i)
l2=[]
k=int(input("enter number of elements:"))
for i in range(0,k):
    i=int(input())
    l2.append(i)
a=len(l1)
b=len(l2)
if (a==b):
    print("The lists are of same length")
else:
    print("The lists are not of same length.")
c=sum(l1)
d=sum(l2)
if(c==d):
    print("sum of the elements of the lists are same")
else:
    print("sum of the elements of the lists are not same.")
e=list(set(l1).intersection(l2))
print("common elements are:",e)
