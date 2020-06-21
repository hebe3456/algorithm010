#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse函数
        # s.reverse()

        # 双指针
        # 时间复杂度：O(N)。执行了 N/2 次的交换。
        # 空间复杂度：O(1)，只使用了常数级空间。
        # 44ms

        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
            # l += 1
            # r -= 1
        return s


s = Solution()
print(s.reverseString(["h","e","l","l","o"]) )

# @lc code=end