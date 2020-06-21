/*
 * @lc app=leetcode.cn id=344 lang=java
 *
 * [344] 反转字符串
 */



// @lc code=start
class Solution {
    public void reverseString(char[] s) {
        // 思路：收尾交换，双指针 1ms, 99.9%
        int l = 0, r = s.length - 1;
        while (l < r) {     // < 即可，<=多交换了一次中间字符（自己跟自己交换）
            char tmp = s[l];
            s[l++] = s[r];
            s[r--] = tmp;
        }
    }
}





// @lc code=end

