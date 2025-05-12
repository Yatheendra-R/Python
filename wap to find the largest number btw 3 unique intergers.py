#wap to find the largest number btw 3 unique intergers
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the first number:"))
if a>b and a>c:
    print(a,"is a largest number")
if b>a and b>c:
    print(b,"is a largest number")
if c>a and c>b:
    print(c,"is a largest number")
if a==b and b==c and c==a:
    print(a,",",b,"and",c,"are equal")
    print("All the three intergers are equal")
    
