#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations1(self, digits: str) -> List[str]:
        # time: 32ms, beats 94.95%
        # define a dict
        num_letter_dict = {'2': 'abc', '3': 'def',  
                            '4': 'ghi', '5': 'jkl',
                            '6': 'mno', '7': 'pqrs',  
                            '8': 'tuv', '9': 'wxyz' }
        if len(digits) == 0: 
            return []
        if len(digits) == 1:
            return list(num_letter_dict[digits[0]])
        # similar to "ziji": previous + the last one
        prev = self.letterCombinations(digits[:-1])
        additional = num_letter_dict[digits[-1]]
        return [s + c for s in prev for c in additional]


    def letterCombinations(self, digits: str) -> List[str]:     
    # backtracking
    # 52ms, beats 12.36%
    if not digits:
        return []
    num_letter_dict = {'2': 'abc', '3': 'def',  
                '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs',  
                '8': 'tuv', '9': 'wxyz' }
    res = []
    self.helper(digits, num_letter_dict, 0, "", res)
    return res

    def helper(self, digits, num_letter_dict, idx, path, res):
    if len(path) == len(digits):
        res.append(path)
        return

    for i in range(idx, len(digits)):
        for j in num_letter_dict[digits[i]]:
            self.helper(digits, num_letter_dict, i + 1, path + j, res)


# @lc code=end

