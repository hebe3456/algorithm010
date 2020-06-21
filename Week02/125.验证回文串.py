#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
# 
# 基础：首先生成新字符串（去掉字母数字以外字符） + 切片：[] == [::-1] 或者 reversed()函数
# 优化：首先生成新字符串（去掉字母数字以外字符） + 双指针法
# 时间复杂度：O(|s|)，其中 |s|是字符串 s 的长度。
# 空间复杂度：O(|s|)。将所有字母和数字字符存放在另一个字符串中，在最坏情况下，新的字符串 与原字符串 s完全相同

# 优化：双指针法直接遍历原字符串
# 时间复杂度：O(|s|)，其中 |s|是字符串 s 的长度。
# 空间复杂度：O(1)

# @lc code=start
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        # 双指针法  60ms
        if len(s) <= 1:
            return True
        l, r = 0, len(s)-1
        while l < r:
            # 如果不是字母和数字，就移动指针
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # 如果不等，返回False；相等，移动指针
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub(r'\W+','',s)
        # s = re.sub('[^a-z0-9]+','',s)
        return s == s[::-1]

# @lc code=end

