n = int(input("enter the limit:"))
n1 = 0
n2 = 1
count = 0
if (n == 1):
    print("fibonacci series upto", n, ":")
    print(n1)
else:
    print("fibonacci series:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
