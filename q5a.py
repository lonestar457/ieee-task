def gmi(l, n=3):
        return sorted(range(len(l)), key=lambda i: l[i], reverse=True)[:n]
def x(ip):
    a=[]#list of all the inputs
    b=[]
    for i in ip:
        for j in i:
            a.append(j)
    for x in a:
        b.append((x,a.count(x)))
    d=[]#list with pro and their count
    for x in b:
        if x not in d:
                d.append(x)
    no=1
    for i in ip :#cust
        c=[]
        for j in i :
            for x in range (0,len(d)):
                if j==d[x][0]:
                    c.append((j,d[x][1]))
        s=[]#selecting max three 
        for i in c:
            s.append(i[1])
        
        k=gmi(s)
        print ("customer ",no)
        for i in k :
            print("The recommendation for custmore is product : ",c[i][0]," which is searched ", c[i][1] , " times") 
        no+=1
ip = eval(input ("Enter data : "))
x(ip)
# without the use of dictionary, alternate soln in que 5 b 
# the example array is not correct for question 5a perhaps its a example for 5b
