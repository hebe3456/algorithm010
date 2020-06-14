#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne2(self, digits: List[int]) -> List[int]:
        # 数学方法
        # 因为+1只有两种情况：10需要进位：小于10不需要进位
        # 从数组尾部遍历
        # 如果遇到数字不是9就+1，并返回
        # 如果是9，则将当前数字置0，并进入下一轮循环
        # 考虑特殊情况：9999，最后一次for循环的数字是0
        # 此时在数组最前面加一个数字1，然后返回即可
        # 36ms
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits        #
            digits[i] = 0
        return [1] + digits

        # # 32ms 95.48%   top tips1 hard to understand...
        # digits[-1] += 1
        # for i in range(len(digits)-1, 0, -1):
        #     if digits[i] != 10:
        #         break
        #     digits[i] = 0
        #     digits[i-1] += 1

        # if digits[0] == 10:
        #     digits[0] = 0
        #     return [1] + digits
        # return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        # 数学取模方法
        # 因为+1只有两种情况：10需要进位：小于10不需要进位
        # 从数组尾部遍历
        # 如果遇到数字不是9就+1，并返回
        # 如果是9，则将当前数字置0，并进入下一轮循环
        # 考虑特殊情况：9999，最后一次for循环的数字是0
        # 此时在数组最前面加一个数字1，然后返回即可
        # 44ms, 没懂。。。
        carry = 1
        for i in range(len(digits)-1, -1, -1):
           carry, digits[i] = divmod(digits[i] + carry, 10)      #
        if carry:
            digits.insert(0, carry)
        return digits


    def plusOne1(self, digits: List[int]) -> List[int]:
        # 暴力：转成int, +1, 转成数组
        # 注意：数组中的值是int，需要转换！！！太麻烦
        # time: O（N）
        # space: 0(N)
        # 60ms
        digits_str = []
        for num in digits:
            digits_str.append(str(num)) 
        num = int("".join(digits_str))
        num += 1
        res = []
        for num in list(str(num)):
            res.append(int(num))
        return res


# @lc code=end

