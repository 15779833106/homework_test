def hanoi(n,source,target,helper):
    if n==1:
        move(source,target)
    else:
        hanoi(n-1,source,helper,target)  #A-C
        move(source,target)      #A-B
        hanoi(n-1,helper,target,source)  #C-B

def move(source,target):
    disk=source[0].pop()
    print(source[1],target[1])
    target[0].append(disk)


source=[[3,2,1],'A']
target=[[],'B']
helper=[[],'C']
print(hanoi(3,source,target,helper))
print(target)






