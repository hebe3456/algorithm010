import javax.sound.sampled.SourceDataLine;

/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        // 只遍历一次数组：O(N); 没有格外使用空间：O(1)
        // 定义赋值左右指针
        int l = 0, r = height.length - 1;
        // 定义赋值左右指针最大值和结果
        int l_max = 0, r_max = 0, ans = 0;
        while (l < r) {
            System.out.println(l,r); 
            if (height[l] < height[r]) {
                // 如果左指针柱子高度 小于 右指针柱子高度，说明应该用右指针坐右边界，移动左指针
                // 找到l_max，累积积水量
                if (height[l] > l_max) {
                    // 如果左指针当前高度 大于 l_max，就赋值给l_max
                    l_max = height[l];
                }else {
                    // 如果左指针当前高度 小于 l_max，就证明存在低洼
                    // 将积水量加入答案，因为长度为1，就只记高度就好
                    ans += l_max - height[l];
                }
                l ++;
            } else {
                // 如果左指针柱子高度大于右指针柱子高度，说明应该用左指针坐左边界，移动右指针
                if (height[r] > r_max) {
                    r_max = height[r];
                } else {
                    // 如果右指针当前高度 小于 r_max，就证明存在低洼
                    // 将积水量加入答案，因为长度为1，就只记高度就好
                    ans += r_max - height[r];
                }
                r ++;
            }
        }
        return ans;
    }
}
// @lc code=end

