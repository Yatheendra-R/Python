#factors of given number
num=int(input("Enter the number:"))
n=int(input("Enter the number of factors:"))
for i in range(1,n):
    if num%i==0:
        print(i,"factors of given number")
