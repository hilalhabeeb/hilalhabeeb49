num=int(input("Enter the number to find the factorial:"))
fact=1
if(num<0):
    print("factorial doesnt exist for negative numbers.")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of",num,"is",fact)
