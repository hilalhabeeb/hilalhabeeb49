def factors():
    n = int(input("enter the number"))
    for i in range(0,n):
        if n%i==0:
            print(i)


factors()