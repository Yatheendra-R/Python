#wap to find positive, negative and zero number
x=int(input("Enter the number of times to find the number is positive or negative or zero:"))
for i in range(x):
    n=float(input("Enter the number:"))
    if n==0:
        print(n,"is equal to zero")
    if n>0:
        print(n,"is a positive number")
    if n<0:
        print(n,"is a negative number")

