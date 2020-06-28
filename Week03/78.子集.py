#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start

# 算法：找重复子步骤，
# n个元素所有子集，就是 n-1个元素的所有子集，分别 + [n]
# 时间复杂度：O(N * 2^N)，生成所有子集，并复制到输出结果中。
# 空间复杂度：O(N × 2^N), 这是子集的数量。
# 对于给定的任意元素，它在子集中有两种情况，存在或者不存在（对应二进制中的 0 和 1）。因此，NN 个数字共有 2^N 个子集。

class Solution:
    def subsets(self, nums):
        res = [[]]         # 里面的[]
        # time: 40
        for num in nums:
            res += [[num] + sub_set for sub_set in res]
        return res


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # time: 4oms
        result = [[]]

        for num in nums:
            newsets = []
            for subset in result:   
                new_subset = subset + [num]
                newsets.append(new_subset)

            result.extend(newsets)
        return result


# @lc code=end

