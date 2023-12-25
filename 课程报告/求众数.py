def majorElement(nums):
    res= getMajor(nums, 0, len(nums) - 1)
    return res

def getMajor(nums,left,right):
    if left==right:
        return nums[left]
    mid=(left+right)//2
    leftMax=getMajor(nums,left,mid) #求左边的众数
    rightMax=getMajor(nums,mid+1,right) #求右边的众数
    if leftMax==rightMax:  #如果两边众数相等则直接返回
        return leftMax
    leftCount=0
    rightCount=0
    for i in range(left,right+1):#左右两边众数不等，进行计数
        if nums[i]==leftMax:
            leftCount+=1
        if nums[i]==rightMax:
            rightCount+=1
    return leftMax if leftCount>rightCount else rightMax  #选择个数多的为众数


if __name__=="__main__":
    nums=[4,3,4,4,3]
    print(majorElement(nums))