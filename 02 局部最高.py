def jubuzuigao(lst):
    res=[]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i+1==len(lst):lst[i+1][j]=-9999
            if j+1==len(lst[i]):lst[i][j+1]=-9999
            if i-1==-1:lst[i-1][j]=-9999
            if j-1==-1:lst[i][j-1]=-9999
            if lst[i][j]>max(lst[i+1][j],lst[i-1][j],lst[i][j+1],lst[i][j-1]):
                res.append(lst[i][j])
    return res

list1=[[3,8,21,13],[1,10,6,12],[15,9,11,17],[16,17,19,20]]
print(jubuzuigao(list1))



