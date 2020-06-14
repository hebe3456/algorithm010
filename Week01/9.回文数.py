#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 暴力法：
        # 如果是负数，return False
        # 如果是正数，列表或字符串切片
        # str:80ms, 80.33%
        # list:100ms, 35.03%
        if x < 0: return False
        if len(str(x)) < 2: return True
        return str(x) == str(x)[::-1]
        # return list(str(x)) == list(str(x))[::-1]

s = Solution()
print(s.isPalindrome(-234))
print(s.isPalindrome(0))
print(s.isPalindrome(3))
print(s.isPalindrome(1328))
print(s.isPalindrome(3443))
# @lc code=end

