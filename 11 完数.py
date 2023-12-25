res=[]
for i in range(2,1001):
    temp1=[]
    for j in range(1,i//2+1):
        if i%j==0:
            temp1.append(j)
    if sum(temp1)==i:
        res.append(i)
print(res)

#输出：[6, 28, 496]