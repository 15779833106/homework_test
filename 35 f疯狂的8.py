import numpy
def isMatch(c1,c2):
    if c1[0]==c2[0] or c1[1]==c2[1]:  #相同面值，相同花色
        return True
    if c1[0]=='8' or c2[0]=='8':   #一张有8
        return True
    return False
def crazyEight(cards):
    trick={}
    parent={}
    trick[0]=1
    parent[0]=None
    for i,ci in enumerate(cards):
        tempTrick=[]
        if i>0:
            for j,cj in enumerate(cards[:i]):
                if isMatch(ci,cj):
                    tempTrick.append(trick[j])
                else:
                    tempTrick.append(0)
            maxTrick=max(tempTrick)
            trick[i]=maxTrick+1
            idxMax=numpy.argmax(tempTrick)
            if isMatch(ci,cards[idxMax]):
                parent[i]=idxMax
            else:
                parent[i]=None
    return trick,parent
def getLongestList(trick,parent):
    longestList=[]
    idxMax=0
    for i in range(len(trick)):
        idxMax=i if trick[i]>trick[idxMax] else idxMax
    while idxMax!=None:
        longestList.append(idxMax)
        idxMax=parent[idxMax]
    longestList.reverse()
    return longestList
if __name__=="__main__":
    cards=['7c','7h','Kc','Ks','8h']
    trick,parent=crazyEight(cards)
    lis=getLongestList(trick,parent)
    print(lis)
    print("最长序列长度为："+str(len(lis))+"\n具体序列为:",end="")
    for i in lis:
        print(cards[i],end=" ")

