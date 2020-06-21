#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# 暴力，遍历整个数组，找到最小元素
# time: O(N) N 给定数组长度

# 优化：改进二分搜索：找到中间点，根据条件决定是取左半还是右半
# 二分搜索应用前提：升序
# 升序且无重复值，旋转一次，
# 找规律：
# 算法：
# 如果尾元素 > 头元素，未旋转
# 如果尾元素 < 头元素，旋转，尾元素后一个元素是头元素(可能中间不连接？)，此时中间有个变化点，需要找到
# 找到中间元素 mid，
# 如果 mid > 0元素，变化点在mid右边 
# 如果 mid < 0元素，变化点在mid左边
# 找到变化点停止搜索，判断满足如下条件即可：（和左右两边值比较，返回小的!）
# 如果 nums[mid] > nums[mid + 1], mid+1 是最小值
# 如果 nums[mid - 1] > nums[mid], mid 是最小值
# 40ms
# time: O(logN)
# space: O(1)

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 特例处理
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        if nums[r] > nums[l]: return nums[0]
        while l < r:
            # mid = l + (r - l)//2             # 二者没太大区别，
            mid = (l + r)//2
            if nums[mid] > nums[mid + 1]:    # mid + 1
                return nums[mid + 1]         # 返回小的
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        

# @lc code=end

