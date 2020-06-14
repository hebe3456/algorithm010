#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # @param nums, a list of integer
        # @param k, num of steps
        # @return nothing, please modify the nums list in-place.
        # 审题：右移是什么意思，末位放到首位，也就是右移一位，前面多一个元素

        # 1 切片
        # 44ms
        # nums_len = len(nums)
        # k = k % nums_len
        # nums[:] = nums[-k:] + nums[:-k]              # same time

        # nums[:] = nums[nums_len-k:] + nums[:nums_len - k]        # 
        # The above one can truly change the value of old nums, but the following one just changes its reference to a new nums not the value of old nums.
        # nums = nums[nums_len-k:] + nums[:nums_len - k]
        # but the above one just changes its reference to a new nums not the value of old nums.


        # 2 Classical 3-step array rotation:？？？
        # reverse the first n - k elements
        # reverse the rest of them
        # reverse the entire array
        # O(n) in time, O(1) in space
        # 48ms   47.74%

        if k == None or k <= 0: return 
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, end)
        # self.reverse(nums, 0, end - k)
        # self.reverse(nums, end - k + 1, end)
        # self.reverse(nums, 0, end)

    # reverse int list from start to end
    def reverse(self, nums, start, end):       # 层级
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end -1


        # 暴力
        # Rotate k times:
        # Each rotation, we move the n - 1 to the back of the array one by one and we do rotation k times.
        
        


# @lc code=end

