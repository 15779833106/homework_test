def L(A,x):
    left,right=0,len(A)-1
    if A[-1]<x:
        return False
    while left<right:
        mid=(left+right)//2
        if x>A[mid]:
            left=mid+1
        else:
            right=mid
    return left

A=[0,1,1,2,3,3,3,3,4,5,5,7,7,7]
print(L(A,5))

