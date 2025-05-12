#difference btw break and continue
#break(output=he)
s="hello"
s1=""
for i in range(len(s)):
    if i==2:
        break
    else:
        s1=s1+s[i]
print(s1)
#continue(output=helo)
s="hello"
s1=""
for i in range(len(s)):
    if i==2:
        continue
    else:
        s1=s1+s[i]
print(s1)
