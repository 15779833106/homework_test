def merge(list1,list2):
    temp=[]
    min1=min(len(list1),len(list2))
    l1=0
    l2=0
    while l1<len(list1) and l2<len(list2):
        if(list1[l1]<=list2[l2]):
            temp.append(list1[l1])
            l1+=1
        else:
            temp.append(list2[l2])
            l2+=1
    for m in range(l1,len(list1)):
        temp.append(list1[m])
    for n in range(l2,len(list2)):
        temp.append(list2[n])
    return temp


def merge_sort(a):
    if len(a)<=1:
        return a
    middle=len(a)//2
    list1=a[:middle]
    list2=a[middle:]
    left=merge_sort(list1)
    right=merge_sort(list2)
    return merge(left,right)


print(merge_sort([6,7,4,3,6,1,9,45,89]))