def quickSort(a,left,right):
    if left>=right:
        return
    l=left
    r=right
    temp=a[left]
    while l<r:
        while a[r]>=temp and l<r:
            r=r-1
        while a[l]<=temp and l<r:
            l=l+1
        a[l],a[r]=a[r],a[l]
    a[l],a[0]=temp,a[l]
    quickSort(a,0,l)
    quickSort(a,l+1,r)
    return a

def mink(a,k):
    res=[]
    quickSort(a,0,len(a)-1)
    for i in range(k):
        res.append(a[i])
    return res

def Nk(a,k):
    res=a[:k]
    for i in range(k,len(a)):
        max = res[0]
        n=0
        for j in range(k):
            if res[j]>max:
                max=res[j]
                n=j
        if a[i] < max:
            res[n]=a[i]
    return res


print(Nk([1,2,3,4,6,7,8],1))
print(mink([5,1,2,3,4,6,7,8],2))
