a=input ("Enter string 1: ")
b=input ("Enter string 2: ")
s=0
for i in a :
    for j in b :
        if i==j:
            s+=1
if s!=0:
    print ("Complimentry, No of matching elements = ",s)
else:
    print ("Not complimentry")