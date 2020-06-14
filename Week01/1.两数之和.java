/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
         *  暴力:遍历两轮循环，判断两个数之和是否为target
         *  O(N*2), O(1)
         *  优化：一轮循环，用字典去存储num 和 索引
         *  表示出另一个值，判断其是否在num前的元素中，在返回；
         *  否则添加到字典
         *  O(N), O(N)   
         *  2ms, 99.62%
         */

        final int [] result = new int[2];
        final Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                result[1] = i;
                result[0] = map.get(target - nums[i]);
                return result;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}
// @lc code=end

