def insert_sort(lst):   #插入排序
    length=len(lst)
    a=lst[0]
    for i in range(1,length):
        j=i-1
        while j>=0:
            if lst[j+1]<lst[j]:
                lst[j+1],lst[j]=lst[j],lst[j+1]
            j=j-1
    return lst
def select_sort(lst):  #选择排序
    length=len(lst)
    for i in range(0,length):
        n=i
        min=lst[i]
        for j in range(i+1,length):
            if lst[j]<min:
                min=lst[j]
                n=j
        lst[i],lst[n]=lst[n],lst[i]
    return lst
def merge_sort(lst): #合并排序
    if len(lst)==1:
        return lst;
    length=len(lst)
    middle=length//2

    return merge(merge_sort(lst[0:middle]),merge_sort(lst[middle:length]))
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
print(insert_sort([6,7,4,3,6,1,9,45,89]))
print(select_sort([6,7,4,3,6,1,9,45,89]))
print(merge_sort([6,7,4,3,6,1,9,45,89]))

