/*
 * @lc app=leetcode.cn id=283 lang=java
 *
 * [283] 移动零
 * 0ms, 100%
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;     // ==
        int j = 0;
        for (int num:nums) {
            if (num != 0) nums[j++] = num;    // don't forget ++  
            // if (num != 0) {
            //     nums[j++] = num;           // don't forget ++  
            // }
        }
        
        while (j < nums.length) {
            nums[j++] = 0;                   // don't forget ++
        }
    }
}
// @lc code=end

