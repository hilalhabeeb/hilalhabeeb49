s1=input("Enter the first string")
s2=input("Enter the second string")
a1=s1[0]
a2=s2[0]
s=a2+s1[1:]+' '+a1+s2[1:]
print(s)