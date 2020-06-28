/*
 * @lc app=leetcode.cn id=50 lang=java
 *
 * [50] Pow(x, n)
 */

// @lc code=start
class Solution {
    public double myPow(double x, int n) {       
        // 取绝对值 1ms, 94.4%
        long m = n > 0 ? n : -(long)n;
        double res = 1.0;
        while (m != 0) {
            if ((m & 1) == 1) {
                res *= x;
            }
            x *= x;
            m >>= 1;
        }
        return n >= 0 ? res : 1 / res;
    }

    public double myPow1(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            // n = -(long)n;   
            // error: incompatible types: possible lossy conversion from long to int
            // long n = -(long)n;
            // error: variable n is already defined in method myPow(double,int)
            long m = -(long)n;
            // n < 0 是赋值给 m， 大于0 时也需要赋值，因此不行。。。
        }
        return 1;
    }
    

    public double myPow2(double x, int n) { 
        /* This is a simple solution based on divide and conquer */
        double tmp = x;
        if (n==0) return 1;
        tmp = myPow(x, n/2);
        if (n % 2 == 0) {
            return tmp * tmp;
        } else {
            if (n > 0) {
                return x * tmp * tmp;
            } else {
                return (tmp * tmp) / x;
            }
        }
    }
}
// @lc code=end

