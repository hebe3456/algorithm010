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
        l_max_height = 0
        r_max_height = 0
        ans = 0
        while (l < r):
            if (height[l] < height[r]):
                # 高的不动，移低的指针，因为：低的里的面积才会积水，高的那部分只有一边，就流出了
                # 如果当前左指针柱子高度 小于 右指针柱子高度，移动左指针：+1
                # 找l_max，累积积水量，因为：左边低会流出去，只有先找到高的，再出现低的，右边有高的，才能积水
                if (height[l] > l_max_height):
                    # 找l_max如果左指针当前高度 大于 l_max，就赋值给l_max
                    l_max_height = height[l]
                else:
                    # 如果左指针当前高度 小于 l_max，就证明存在低洼
                    # 将积水量加入答案，因为长度为1，Area = 高度差
                    ans += l_max_height - height[l]
                l += 1
            else:
                # 如果左指针柱子高度大于右指针柱子高度，移动右指针：-1！！！
                if (height[r] > r_max_height):
                    r_max_height = height[r]
                else:
                    # 如果右指针当前高度 小于 r_max，就证明存在低洼
                    # 将积水量加入答案，因为长度为1，就只记高度就好
                    ans += r_max_height - height[r]
                r -= 1                                # ！！！
        return ans


# @lc code=end

