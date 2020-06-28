#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums):
        # time：44ms beats 93.58%
        res = [[]]
        for num in nums:
            tmp_res = []
            for sub_set in res:
                for i in range(len(sub_set)+1):
                    tmp_res.append(sub_set[:i] + [num] + sub_set[i:])
                    # handle duplication！
                    if i < len(sub_set) and sub_set[i] == num: break       
            res = tmp_res
        return res

s = Solution()
print(s.permuteUnique([1,2,1]))
# @lc code=end

