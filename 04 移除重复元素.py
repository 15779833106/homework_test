def remove_num(list1):
    list1.sort()
    for i in list1:
        if list1.count(i)>1:
            list1.remove(i)
    return list1
print(remove_num([1,2,3,5,4,8,4,2,1,3,5,4]))