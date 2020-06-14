#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 进阶法：
        # 如果是负数，或者是尾数为0的非零数，return False
        # 如果是正数，做数学运算
        # str:80ms, 80.33%
        # list:100ms, 35.03%
        # 108ms，25.36%  貌似更慢。。。
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        return x == self.reverseUtil(x)

    def reverseUtil(self, x):
        result = 0

        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)

        return result


        # 报错
        # if x < 0: return False

        # ranger = 1
        # while x / ranger >= 10:
        #     ranger *= 10

        # while x:
        #     left = x / ranger
        #     right = x % 10
        #     if left != right:
        #         return False

        #     x = (x % ranger) / 10
        #     ranger /= 100

        # return True

s = Solution()
print(s.isPalindrome(-234))
print(s.isPalindrome(0))
print(s.isPalindrome(3))
print(s.isPalindrome(1328))
print(s.isPalindrome(3443))
# @lc code=end

