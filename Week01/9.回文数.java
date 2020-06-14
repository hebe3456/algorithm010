/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        // compare half of the digits in x, so don't need to deal with overflow.
        // 时间复杂度：O(N) 9ms 99.05%
        // 空间复杂度：O(1)
        // 负数，或者末位为0的非零数
        if (x<0 || (x!=0 && x%10==0)) return false;
        int rev = 0;
        while (x>rev) {
            rev = rev * 10 + x % 10;
            x = x/10;
        }
        return (x==rev || x==rev/10);
    }
}
// @lc code=end

