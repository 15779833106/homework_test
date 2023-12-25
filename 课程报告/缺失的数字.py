class Solution:
    """运用哈希集合的方法，先将数值存放如哈希集合中，然后进行遍历查找，单个查找的时间复杂度为O(1),
    整个过程的时间复杂度为O(n),又由于另外构建了集合，因此空间复杂度为O(n)"""
    def missingNumber1(self, nums):
        s = set(nums)  #创建一个哈希集合
        for i in range(len(nums) + 1): #遍历0-n
            if i not in s:  #检查遍历的数值是否在集合中
                return i  #不在，返回缺失数值

    """主要运用数学的求和公式然后进行一个遍历的相减，
    多余的数值即为缺失的数字，时间复杂度为O(n)，空间复杂度为O(1)"""
    def missingNumber2(self,nums):
        sum=(0+len(nums))*(len(nums)+1)//2  #假使不缺失时编号数值的和
        for i in nums: #对编号进行遍历
            sum-=i    #不缺失时的和逐个减去现在的编号，最后的余值即为缺失的编号
        return sum

if __name__=="__main__":
    ls=[0,1,2,3,4,5,7]
    print(Solution().missingNumber1(ls))
    print(Solution().missingNumber2(ls))
