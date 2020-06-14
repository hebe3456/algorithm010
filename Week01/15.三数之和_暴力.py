#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len = len(nums)
        res_dict = {}
        for i in range(nums_len-2):
            for j in range(i+1, nums_len-1):
                for k in range(j+1, nums_len):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res_dict[nums[i],nums[j],nums[k]] = 1
        res_list = []
        for key in res_dict.keys():
            res_list.append(list(key))
        return res_list

s = Solution()
print(s.threeSum([-1,0,-1,1]))
print(s.threeSum([-1,0,-1,1,3,2]))

