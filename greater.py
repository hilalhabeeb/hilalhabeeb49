num1=float(input("enter number one:"))
num2=float(input("enter number two:"))
num3=float(input("enter number three:"))
if(num1>=num2) and (num1>=num3):
    print("num1 is greater ")
elif(num2>=num1) and (num2>=num3):
    print("num2 is greater ")
else:
    print ("num3 is greater")