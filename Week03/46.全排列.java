/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        // time: 2ms beats 81.74%
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (nums.length == 0 ) return res;
        List<Integer> list0 = new ArrayList<Integer>();
        list0.add(nums[0]);
        res.add(list0);

        for (int i = 1; i < nums.length; ++i) {
            List<List<Integer>> new_res = new ArrayList<List<Integer>>();
            for (int j = 0; j <= i; ++j) {
                for (List<Integer> list : res) {
                    List<Integer> new_list = new ArrayList<Integer>(list);
                    new_list.add(j, nums[i]);
                    new_res.add(new_list);
                }
            }
            res = new_res;
        }
        return res;
    }
}
// @lc code=end

