def majorElement(nums):
    def majority_element_rec(low, high):
        if low == high:
            return nums[low]

        mid = (high - low) // 2 + low  #分割
        left = majority_element_rec(low, mid)
        right = majority_element_rec(mid + 1, high)

        if left == right:  #左右区间众数相同
            return left

        #左右区间众数不同，进行计数统计
        left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high + 1) if nums[i] == right)

        return left if left_count > right_count else right
    return majority_element_rec(0, len(nums) - 1)

if __name__=="__main__":
    nums=[1,2,3,4,2,24,2,3,4,1,234,3,3,3,3,3,3,3,3,3,3,3]
    print(majorElement(nums))