dict={}
str1=input("enter the string")

for i in str1:
    if i in dict:
        dict[i]=dict[i]+1
        print(dict)
    else:
        dict[i]=1
        print(dict)
print("character freequency")
for m,n in dict.items():
    print(m,n)




