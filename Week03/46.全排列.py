#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time: 36ms, beats 94.71%
        res = [[]]
        for num in nums:
            tmp_res = []
            for sub_set in res:
                for i in range(len(sub_set)+1):
                    tmp_res.append(sub_set[:i] + [num] + sub_set[i:])    # insert [num]  append!
            res = tmp_res
            # 想用列表生成式，没成功。。。
        return res
# @lc code=end

