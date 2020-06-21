#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        # 1 暴力：两个for循环，外循环遍历单词，内循环遍历单词的字母索引，如果同一索引字母均相同，则加到结果中；不相同，终止跳出循环
        # time: (N*2)    space: O(N) 结果数组
        # 2 按照长度排序，再循环查找
        # 3 直接按长度取最短的字符串即可， 循环用enumerate()
        # time: (N*2)    space: O(1) 
        if not strs: return ""
        shortest_str = min(strs, key=len)
        for idx, letter in enumerate(shortest_str):
            for word in strs:         # 没排序所以要遍历所有单词！
                if letter != word[idx]:
                    return shortest_str[:idx]
        return shortest_str
        
        
# 按照长度排序，再循环：
class Solution2:
    def longestCommonPrefix(self, strs):
        # 44ms 
        if not strs: return ""
        strs.sort(key = len)
        for idx in range(len(strs[0])):
            for word in strs[1:]:
                if strs[0][idx] != word[idx]:
                    # if idx == 0:        a[:0] = ""!
                    #     return ""
                    return word[:idx]
        return strs[0]                     # 缩进层级！
        

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))

# @lc code=end

