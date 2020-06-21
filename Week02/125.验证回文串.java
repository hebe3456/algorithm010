/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() <= 1) {
            return true;
        }

        int l = 0, r = s.length() - 1;
        char cL, cR;
        while (l <= r) {
            cL = s.charAt(l);
            cR = s.charAt(r);
            if (!Character.isLetterOrDigit(cL)) {
                l++;
            } else if (!Character.isLetterOrDigit(cR)) {
                r--;
            } else {
                if (Character.toLowerCase(cL) != Character.toLowerCase(cR)) {
                    return false;                    
                } 
                l++;
                r--;
            }
        }
        return true;
    }
}
// @lc code=end

