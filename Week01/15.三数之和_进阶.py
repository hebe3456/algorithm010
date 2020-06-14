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
        分析
        不重复，但是三个数字可以有重复
        1 暴力
          O(N*3)
        2 想到twoSum， 表示成为: -a = b + c, 用夹逼法
          升序排序
          先判断a，如果大于0，则不可能满足题意，break
          否则：比较 -a 和 b+c
              双指针i，j
              如果 相等，返回结果
              如果 大于，j-1
              如果 小于，i+1
              结束条件：i >= j
          
          O(N*2)
        https://leetcode-cn.com/problems/3sum/solution/man-hua-jue-bu-wu-ren-zi-di-xiang-kuai-su-kan-dong/
        """
        li = []      # 结果是列表，包含多组解
        nums.sort()
        nums_len = len(nums)
        if nums_len < 3:
          return li

        for i in range(nums_len - 2):
            if nums[i] > 0: break                # 跳出次轮循环而已
            if i > 0 and nums[i] == nums[i-1]: continue    # 去重
            l, r = i + 1, nums_len - 1 
            while l < r:                         # 满足的条件
              s = nums[i] + nums[l] + nums[r]    # 循环里
              if s == 0:
                li.append([nums[i], nums[l], nums[r]])    # grammer
                l += 1                                    # 还可能有其他解
                r -= 1
                # 如果相邻两个数相同，则+1或-1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
              elif s > 0:
                r -= 1
              elif s < 0:
                l += 1
        return li

          
s = Solution()
print(s.threeSum([-1,0,-1,2]))
print(s.threeSum([-1,0,-1,1,3,2]))
print(s.threeSum([-1,0,1,2,-1,-4]))


# @lc code=end