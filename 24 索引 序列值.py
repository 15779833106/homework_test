def getIndex(arr):
    length=len(arr)
    left,right=0,length-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]>mid:
            right=mid-1
        elif arr[mid]==mid:
            return f'A[{mid}]={mid}'
        else:
            left=mid+1
    return "不存在"

A=[0,2,2,7,9]
print(getIndex(A))
