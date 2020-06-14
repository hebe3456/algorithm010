#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        # 审题：原地移除，不能有新数组，和移动零类似；排序数组；
        # 返回值是啥？个数
        # time: O(N) space: O(1) 4Oms
        if not nums: return 
        # 定义指针j
        j = 0
        # 比较相邻的数，用索引遍历
        for i in range(1, len(nums)):
            # 如果相等就继续；否则就j+1,再赋值
            if nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
        return j+1    
        # Line 48: TypeError: [1, 2] is not valid value for the expected return type integer[]  应该返回个数


s = Solution()
print(s.removeDuplicates([1,1,2]))

# @lc code=end

