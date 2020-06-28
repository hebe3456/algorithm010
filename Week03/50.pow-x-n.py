#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#


"""
1 暴力
result = 1
for i in range(n):
    result *= x
注意：考虑n为负的情况
time：O(N)

2 分治
template: 
1 terminator    
2 process(split your big problem)
3 drill down (subproblem), merge(subresult)
4 reverse states

x^n --> 2^10：2^5乘以自己  --> (2^2) 乘以自己 [奇偶数问题]
pow(x, n):
    subproblem: subresult = pow(x, n/2)

merge:
    if n % 2 == 1{
        // 偶数 odd
        result = subresult * subresult * x;
    } else {
        // 奇数 even
        result = subresult * subresult;
    }

不论我们返回时候如何，我们执行第一步，先设立Base Case:
if b == 0: return 1

完了以后，我们要对大问题进行拆分，也就是不断的对b的值折半

拆分：
half = self.myPow(a, b // 2)

当拆分到了最小的问题，满足base case b == 0 的时候，我们则进行返回，返回时候有三种可能

Function的三种可能性：
当b为偶数的时候，比如 2 ^ 100，拆分的时候就变成 (2 ^ 50) * (2 ^ 50)
当b为基数的时候，比如 2 ^ 25，拆分的时候就变成 (2 ^12) * (2 ^ 12) * 2
当b为负数的时候，返回 1.0 / self.myPow(a, -b)

时间复杂度 = 一叉树里面每层的时间复杂度 * 层数 = 1 * log(b) = log(b)
空间复杂度 = O(h) 也就是一叉树的层数 = log(b)
https://leetcode.com/problems/powx-n/discuss/182026/Python-or-Recursion-tm
"""

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # time: 32ms, beats 97.1%
        # 二进制，分治，比用绝对值快，最优！！！
        if n < 0:        # error: n not x 
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n & 1:     # &和   偶数 & 1 = 0; 奇数 & 1 = 1;
                res *= x
            x *= x
            n >>= 1       
            # n = n>>1; 就是n变成 n向右移一位的那个数
            # >>是移位运算符，比如 3>>1 就是将3的二进制向右移移位： 
            # 11（3的二进制）向右移移位变成 1，低位自动消失。
        return res

    def myPow1(self, x: float, n: int) -> float:
        # 44ms, beats 50.26%
        # 二进制，分治
        m = abs(n)
        res = 1.0
        while m:
            if m & 1:
                res *= x
            x *= x
            m >>= 1
        return res if n >= 0 else 1 / res

    def myPow2(self, x: float, n: int) -> float:
        # 40ms, beats 74.38%
        # 回归
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)     # -n
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
        

# @lc code=end

