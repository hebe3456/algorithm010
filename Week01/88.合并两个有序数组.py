#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # return nums1.extend(nums2)
        # 审题：nums1 nums2 和生成的均是有序数组；不用额外空间
        # m 和 n ！！！
        # 暴力：遍历nums2， 找到每一个元素在nums1的位置，大于等于前一个元素，小于后一个元素...出不来
        
        # 倒序遍历，取最大的放在最后一个元素位置，向前推
        # while m > 0 and n > 0:
        #     if nums1[m-1] >= nums2[n-1]:
        #         nums1[m+n-1] = nums1[m-1]
        #         m -= 1
        #     else:
        #         nums1[m+n-1] = nums2[n-1]
        #         n -= 1
        # # deal with: nums1:[0], nums2[1]
        # if m == 0 and n > 0:
        #     nums1[:n] = nums2[:n]
        # return nums1

        # 优化  40ms 
        while  n > 0:
            # if m == 0 each num is 0, smaller than num in nums2
            if m == 0 or nums2[n-1] > nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        return nums1
    

# @lc code=end


        # for num in nums2:
        #     if num <= nums1[0]:
        #         nums1.insert(num)
        #         m += 1
        #     if num >= nums1[m-1]:         # 最后一个非零数？？用m去表示！！！
        #         nums1[m] = num
        #     for i in range(m):
        #         if num >= nums1[i] and num < nums1[i+1]:
        #             nums1.insert(i+1, num)

        # return nums1