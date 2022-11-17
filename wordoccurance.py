dict={}
word=input("enter the string")

wrd=word.split(' ')

for i in wrd:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print("word occurance")
for m,n in dict.items():
    print(m,n)



