# 多数元素#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# 已经不是暴力了：遍历生成字典，value > n/2
# time: O(N) 
# space: O(N)
# 80ms, 13.27%

# 优化：sort升序排列，中间元素就是
# time: O(NlogN) !!!
# space: 自带排序算法，用O(logN)的栈空间，自己写堆排序，用O(1) !!!
# 52ms, beats 68.69%

# 

# @lc code=start
class Solution:
    def majorityElement1(self, nums):
        # 52ms, beats 68.69%
        # both are ok
        return sorted(nums)[len(nums)//2]     # sorted
        # nums.sort()
        # return nums[len(nums)//2]    # even odd same


    def majorityElement(self, nums):
        # 80ms, 13.27%
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        for key, value in num_dict.items():    # items()
            if value > len(nums)/2:     # error: nums not num_dict
                return key


s = Solution()
for i in [[1], [3,2,3], [2,2,1,1,1,2,2], [8,8,7,7,7]]:
    print(s.majorityElement(i))

# @lc code=end

