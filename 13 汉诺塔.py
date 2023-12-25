from time import time


def hanoi(n,source,target,helper):
    if n==1:
        moveSingleDesk(source,target)   #当圆盘=1，直接移动到目标柱
    else:
        hanoi(n-1,source,helper,target) #
        moveSingleDesk(source,target) #
        hanoi(n-1,helper,target,source) #

def moveSingleDesk(source,target):    #移动圆盘函数
    disk=source[0].pop()
    print("moving "+str(disk)+" from "+source[1]+" to "+target[1])
    target[0].append(disk)

if __name__=='__main__':
    start=time()
    for i in range()
    A=([10,9,8,7,6,5,4,3,2,1],'A')
    B=([],'B')
    C=([],'C')   #各柱子初始状态
    hanoi(len(A[0]),A,B,C)
    over=time()
    print(over-start)