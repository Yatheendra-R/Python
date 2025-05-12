#wap to accept a character from user and print whether the user entered a alphabet,vowel,consonants,digit and white space 
ch=input("Enter any character from the keyboard:")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print("You have entered an alphabet")
if ch in 'aeiouAEIOU':
    print("You have entered a vowel")
if ch>='b' and ch<='z' and ch not in 'aeiou' or ch>='B' and ch<='Z' and ch not in 'AEIOU':
    print("You have entered a consonent")
if ch>='0' and ch<='9':
    print("You have entered a digit")
if ch==" " or ch=="\n":
    print("You have entered a white space")


    
