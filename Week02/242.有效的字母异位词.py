#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 审题：大小写问题
        # 含有的字母个数相同
        # 两个字典，用字典统计字母出现的次数，两个字典相等
        # O(N)
        # 一个字典，一个+， 一个 -， 最后次数均为0
        # O(N)

        # 两个字典
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1
        return s_dict == t_dict
        
# @lc code=end

