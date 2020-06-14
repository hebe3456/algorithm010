#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#
# 移动零
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (61.03%)	600	-
# Tags
# Companies
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        分析
        算法1：新建两个数组，不是0的元素放一个，是0的元素放一个，合并
        算法2：定义一个指针j，表示插入元素的位置，先插入非0，后插入0
               遍历数组，不是0就插入，全部插入后，余下位置补0
               时间复杂度：O(N), 2个循环
               空间复杂度：O(1), 没有新建数组
               16ms   95.36%
        """
        if nums == None or len(nums) == 0: return   # 必要吗
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
            
        while j < len(nums):
            nums[j] = 0
            j += 1

        """       
        # 指针 + 一轮循环 【快排思想（交换元素）】
        # 1 指针j = 0，遍历数组元素，如果nums[i]不等于0，就和nums[j]交换元素，j += 1

        nums_len = len(nums)
        j = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                
        return nums


        # 指针 + 一轮循环 
        # 指针j = 0，遍历数组元素，如果nums[i]不等于0，赋值给nums[j]，
        #     如果i！= j，就nums[i] = 0
        #     j += 1

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    # 如果i=j，则nums[i] = nums[j], 如果i！= j，则nums[i] = 0
                    # 不太好想，再想想
                    nums[i] = 0
                j += 1
        return nums
        """

# @lc code=end

