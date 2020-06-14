/*
 * @lc app=leetcode.cn id=26 lang=java
 *
 * [26] 删除排序数组中的重复项
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        // 1ms  98.33%
        int j = 0;
        for (int n : nums) {
            if (j == 0 || n > nums[j-1]) {    //
                nums[j++] = n;                //
            }
        }
        return j;                             //

        // 2..
        // int i = nums.length > 0 ? 1 : 0;
        // for (int n : nums)
        //     if (n > nums[i-1])
        //         nums[i++] = n;
        // return i;
    }
}
// @lc code=end

