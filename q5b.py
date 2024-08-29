# there can never ba a case when there are less than three reccomendation. it can only happen when the coustmer hasnt searched for three items yet 
# with dictionary 
ip= [[1,2],[1,2,4,5],[1,3,4,5],[2,3,5],[1,2,3]]
a=[]
for i in ip :
    for j in i :
        a.append (j)# list of all searches 
x=[]#product list
b={}# product with count 
for i in a :
    if i not in x :
        x.append (i)
for i in x :
    b[i]=a.count(i)
#cust
for i in ip :
    print ("coustomer ", ip.index(i)+1)
    if len(i)<=2:
        B=b.copy()
        for j in i :
            print("The recommendation for custmore is product : ",j," which is searched ",B[j], " times")
            del B[j]
        for i in range (0,3-len(i)):
            print ("Other popular products include :",max(zip(B.values(), B.keys()))[1],"searched : ",B[max(zip(b.values(), B.keys()))[1]], "times ")
# alternate to que 5 a using dictionary 
    else :
        di={}
        for j in i:
            di[j]=b[j]
        for i in range (0,3):
            print ("The recommendation for custmore is product :",max(zip(di.values(), di.keys()))[1],"searched : ",di[max(zip(di.values(), di.keys()))[1]], "times ")
            del di[max(zip(di.values(), di.keys()))[1]]