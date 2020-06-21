#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# 审题：多了一个字母，只含小写字母
# 思路：先排序，然后循环遍历比较，找出多的那个字母
# 两个都sort，然后遍历短字符串所有字母，和长字符串比较，return少的字母
# O(N) 
# 生成字典，key为字母，value为个数，个数不一样，就返回对应的key，太复杂


# @lc code=start

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(sorted_s) > len(sorted_t):
            res = self.helped(sorted_s, sorted_t)    
            # 必须得接收self.fun()的返回值，并return，否则return None
        else:
            res = self.helped(sorted_t, sorted_s)
        return res

    def helped(self, s1, s2):
        # 遍历较短字符串，如果不等，则返回长字符串上的字母，
        for idx, letter in enumerate(s2):      # 低级错误：忘了enumerate！
            if letter != s1[idx]:
                return s1[idx]
        # 否则返回长字符最后一个字母
        return s1[-1] 

s = Solution()
print(s.findTheDifference("abcd", "abcde"))
        
# @lc code=end

