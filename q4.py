b=[]
y=[]
for i in range (0,5) :#taking in 5 input
    a=int (input("Enter the integer: "))
    b.append(a)
for i in b:# list of all divisors of all integers 
    for j in range (1,i):
        if i%j==0:
            y.append(j)
c=[]#list of common divisor
for i in y:
    if y.count(i)==5:
        c.append(i)
print ("gcd == ", max(c))
