#wap to accumulate sum of "n" number
s=0
n=int(input("Enter the limit:"))
for i in range(1,n+1):
    s+=i
    print(s,"each step sum")
print(s,"sum of n number")
