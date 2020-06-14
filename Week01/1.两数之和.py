#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1 暴力，两轮遍历，和 = target
          O(N*2)   O(1) 没用额外数组等
        2 用字典，一轮遍历，生成字典；第二轮遍历，如果 target - num 在 num前面的值列表中 
          O(N)   O(N)
        3 用字典，一轮遍历，如果 target - num 在 字典中！！！不要用列表，慢，就返回，否则就加到字典当中
          O(N)   O(N)
          436ms  if ano_num in nums[:idx]:
          68ms  if ano_num in num_idx_dict:   这个还是快非常多的！！！
        字典：用字典存储，一一对应查找最快，用空间换时间~
        """
        
        if len(nums) < 2: return False
        num_idx_dict = {}

        for idx, num in enumerate(nums):
            # 表示另一个数字another_num
            ano_num = target - num      # 错误：如果放在语句里，记得加括号！
            # 如果another_num num在字典中，就是所求结果，返回索引
            if ano_num in num_idx_dict:             # ！！！
                return [num_idx_dict[ano_num], idx]
            # 否则就加到字典中
            num_idx_dict[num] = idx  
        

# @lc code=end


# s = Solution()
# print(s.twoSum([2,7,11,15], 9))