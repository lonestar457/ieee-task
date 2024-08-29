l=eval (input ("Enter a list : "))
t=int (input ("Enter a integer : "))
a=[]
for i in l :
    for j in l :
        if i+j==t:
            c=(i,j)
            a.append(c)
print (c)