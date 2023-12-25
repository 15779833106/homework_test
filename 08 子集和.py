def subset_sum(lst,target):
    res=[[]]
    temp=[]
    for i in lst:
        res=res+[[i]+j for j in res]
    for num in res:
        if sum(num)==target:
            temp.append(num)
    return temp
list1=[5,-4,2,-2]
print(subset_sum(list1,1))

