def dict_add(dict1,dict2):
    temp={}
    for i in dict1.keys() | dict2.keys():
        temp[i]=sum([dict3.get(i,0) for dict3 in (dict1,dict2)])
    return temp

d1={'a':100,'b':200,'c':300}
d2={'a':400,'b':400,'d':400,'c':300}
print(d1.keys(),type(d1.keys()))
print(dict_add(d1,d2))