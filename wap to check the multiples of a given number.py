#wap to check the multiples of a given number
x=int(input("Enter a number:"))
y=int(input("Enter the limts to find the multiple of the number:"))
for j in range(1,y+1):
    if x%j==0:
        print(j,end=" ")
print("are the multiples of the",x,"till the limt",y)

