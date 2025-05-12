#wap to read the age of a person and check if the person is eligible to vote
g=int(input("Enter the age of the person:"))
if g<18 or g>110:
    print("The person is not eligible for voting")
else:
    print("The person is eligible for voting")
