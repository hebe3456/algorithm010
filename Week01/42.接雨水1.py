#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height):
        # 只遍历一次数组：O(N) 没有格外使用空间：O(1)
        # 44ms, 87.14%
        # 定义赋值当前左右指针
        l, r = 0, len(height) - 1
        # 定义赋值左右指针最大高度和结果
        l_max_height = r_max_height = water = 0

        while l <= r:
            l_max_height, r_max_height = max(l_max_height, height[l]), max(r_max_height, height[r])
            while l <= r and height[l] <= l_max_height <= r_max_height:
                water += l_max_height - height[l]
                l += 1
            while l <= r and height[r] <= r_max_height <= l_max_height:
                water += r_max_height - height[r]
                r -= 1
        return water


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# @lc code=end

