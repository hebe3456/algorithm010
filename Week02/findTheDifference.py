class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        # 两个都sort，然后遍历长字符串所有字母，如果不存在在短字符串中，就return
        # O(N) 48ms
        sort_s = sorted(s)
        sort_t = sorted(t)

        if len(sort_s) > len(sort_t):
            res = self.fun(sort_s, sort_t)     # 必须得接收self.fun()的返回值，并return，否则题目输出为None
            return res
        else:
            res = self.fun(sort_t, sort_s)
            return res
            
    def fun(self, s1, s2):
        # 考虑到不同的是最后一个字符情况, 不能用enumerate()
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                return s1[i]
        return s1[-1]



s = Solution()
print(s.findTheDifference("abcde", "abcd"))
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("abcde", "abde"))