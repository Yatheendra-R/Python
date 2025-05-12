s="123-456-789-0+*1"
for i in s:
    if i=="-":
        continue
    elif i=="*":
        break
    elif i=="+":
        pass
    else:
        print(i,end="")
