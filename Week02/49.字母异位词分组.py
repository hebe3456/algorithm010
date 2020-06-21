#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# 暴力，sorted(单词)，相等就加到同一个列表 
# 暴力，求出每个单词的字母出现次数字典，如果相同，就加到同一个列表
# 字典，用所含字母的元组做key，value是个列表，放所有的字符串
# 时间复杂度O(M*N)，N是字符串个数，M是平均字符串长度  ??
# 空间复杂度O(N)

# @lc code=start
class Solution:
    def groupAnagrams(self, strs):

        d = {}
        for w in sorted(strs):              # sorted()去重
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())             # list()

        # for word in strs:
        #     key = tuple(sorted(word))
        #     if key in d:
        #         d[key] += [word]
        #     else:
        #         d[key] = [word]


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# @lc code=end

