### 动态规划DP

1. 重复性（分治）-- 子问题

2. 定义状态数组

3. DP方程

   可以从上往下，也可从下往上



#### [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)[简单]

```
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
```

分析：

暴力：枚举所有的起点和终点，求和，比较求出最大值，time：o(n*2)

优化：不能以负数开头或结尾，因为是连续的，所以首或尾为负数，和会变小

DP：

a 分治（子问题）: max_sum(i) = max(max_sum(i-1), 0) + sums[i]

b 状态数组定义:  dp[i]

c dp方程: dp[i] = max(nums[i], nums[i] + dp[i-1])

最大子序和 = 当前元素自身最大，或是：包含之前后最大

代码

不用新数组dp[]，直接在原数组修改

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp 16ms
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        for i in range(1, len(nums)):          
            # error: 从1开始，因为如果0，i-1不存在-- 共性需要讨论的，其实就是边界值
            nums[i] = max(nums[i], nums[i-1]+nums[i])     # error: nums[i]
        return max(nums)
```



用新数组dp

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
```



优化space：在原数组更新！！！！

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 审题：最大和的连续，return max_sum
        # dp dp[n] = max(dp[n-1], dp[n-1] + sums[n]) 
        # 在原数组更新最大值
        # time：O(N)
        # sapce：O(1)
        # 36ms
      
        if not nums: return None
        if len(nums) == 1: return nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], (nums[i] + nums[i-1]))

        return max(nums)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
```



#### [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/) 【中等】

```
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

https://leetcode-cn.com/problems/triangle/solution/zui-xiang-xi-de-dong-tai-gui-hua-mei-yi-bu-qing-qi/

https://leetcode-cn.com/problems/triangle/solution/120-san-jiao-xing-zui-xiao-lu-jing-he-by-alexer-66/

国际站高票回答：

https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)

**审题：**

每次只能移动到下一行中相邻的结点上

相邻的结点：下标 与 上一层结点下标相同或者等于 上一层结点下标 + 1 的两个结点。

<img src="C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200713114055539.png" style="width:80%;height:30%"/>

算法：

1.**brute-force暴力**， 递归，n层：left or right 2^n

2.DP

**从下往上：**更简单，看这个

<img src="C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200713143753844.png" style="width:50%;height:30%"/>



重复性（分治）；problem(i,j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i,j]

定义状态数组；F[i,j]

DP方程  problem[i,j] = min(sub[i+1, j], sub[i+1, j+1]) + a[i,j]

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom-up
        # time:O(N^2)
        # space:O(N)
        # 44ms
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):    # 倒数第二行开始
            for j in range(i+1):                    # i+1，len(triangle[i]) 也可以
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])   # error：min(,)

        # 第一行是列表，因此需要加[0]变成元素
        return dp[0][0]  
```

空间优化：在triangle上直接修改



**从上往下：**

分三种情况，如上图

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle     #这边的初始化真的是牛逼，不仅不需要把把上面两行特殊的情况考虑进去，而且为下面也做了铺垫。因为是做累加，所以不需要初始化为0       
        #dp是一个list列表，同样也可以看成是一个二维数组，如图所示
        # [             [
        #     2,          [2],
        #     3,4        [3,4],
        #     6,5,7     [6,5,7],
        #     4,1,8,3  [4,1,8,3]
        # ]             ]
        # 可以知道3的下一行中相邻的结点为6和5，6的下一行中相邻的结点为4和1，5的下一行中相邻的结点为1和8

        for i in range(1, len(dp)): # 对第一行的元素，不需要初始化。如:到2的最短路径就是2
            for j in range(i+1):    # i+1
                if j == 0:
                    # 第一列的元素来源路径，只可能是由上一行对应列的元素移动而来   
                    dp[i][j] += dp[i-1][j]          
                if j> 0 and j == i:
                    # 在对角线上的元素 如: 4的来源路径只有可能是从2来
                    # PS:虽然在上面左边图中,4和6好像是相邻的，但是在三角形中，4和6不相邻  
                    # 我的理解就是根据题目要求得到上面左边的图，移动方式只有向下和像45度方向移动两种情况
                    dp[i][j] += dp[i-1][j-1]
                elif (j > 0 and j < i):
                    #求两种移动路径的最小值
                    dp[i][j] += min(dp[i-1][j-1],dp[i-1][j]) 
        return (min(dp[len(triangle)-1]))     # 最后一行是个列表，取其中最小的

s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
```



#### [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)[中等]

```
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
```

分析：dp

方法一：从上到下

原数组，grid(i, j) 表示从坐标 (i, j)**到右下角的最小路径权值**。

分四种情况：**第一个值不变，**第一行，第一列，其他

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # 处理第一行列，除第一个值之外
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        # 处理第一行，除第一个值之外
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        # 其他元素
        for i in range(1, m):           # error: 1
            for j in range(1, n):       # error: 1
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
```

另一种写法：合起来，但是上面的好一点儿，没有判断

```python
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue       # error：！
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

```



方法二：从下到上

我们新建一个额外的 dp 数组，与原矩阵大小相同。在这个矩阵中，dp(i, j) 表示从坐标 (i, j)**到右下角的最小路径权值**。我们初始化右下角的 dp 值为对应的原矩阵值，然后去填整个矩阵，对于每个元素考虑移动到**右边或者下面**，因此获得最小路径和我们有如下递推公式：

dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))

三种情况如下：

<img src="C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200718091935203.png" alt="image-20200718091935203" style="zoom:50%;" />

<img src="C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200718092007357.png" alt="image-20200718092007357" style="zoom:50%;" />

<img src="C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200718091825751.png" alt="image-20200718091825751" style="zoom: 50%;" />





#### [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)[中等]

[1、2【0714】]

```
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

审题：乘积最大，连续，return：乘积

分析：

DP，dp[i] = max(nums[i], dp[i-1] * nums[i])

因为乘积，有正负的问题，因此要维护max_dp 和 min_dp 两个数组！

两个列表指向同一内存地址，一个值改变了，两个都会变！！！如下是错误的：

```python
    # max_dp = min_dp = nums[:]   
    # min_dp = max_dp = [0] * nums_len
```


```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 审题：乘积最大，连续，return：乘积
        # dp dp[i] = max(nums[i], dp[i-1] * nums[i])
        # 有负数，维护max 和 min 两个数组
        # time: O(N)
        # space: O(N)
        # 40ms，98.5%

        if not nums: return 0
        nums_len = len(nums)
        if nums_len == 1: return nums[0]

        # error: 两个指向同一内存地址，所以一个变了，两个都会变！！！
        # max_dp = min_dp = nums[:]   
        # min_dp = max_dp = [0] * nums_len      
        max_dp = [0] * nums_len
        min_dp = [0] * nums_len
        max_dp[0] = min_dp[0] = nums[0]               # error：must have, or max_dp[0]=0
        # 另一种赋值
        dp_max = nums[0] * nums_len
        dp_min = nums[0] * nums_len

        for i in range(1, nums_len):
            tmp = (nums[i], max_dp[i-1] * nums[i], min_dp[i-1] * nums[i])  
            # error: max_dp[i-1] 要有[i-1]，注意类型一致，int 和 list X
            max_dp[i] = max(tmp)
            min_dp[i] = min(tmp)

        return max(max_dp)
    
    

```

另一种写法：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 审题：乘积最大，连续，return：乘积
        # dp dp[i] = max(nums[i], dp[i-1] * nums[i])
        # 优化space，在原数组修改

        maxDp = [nums[0]]
        minDp = [nums[0]]
        for i in nums[1:]:
            tmp = (i*maxDp[-1], i*minDp[-1], i)
            maxDp.append(max(tmp))
            minDp.append(min(tmp))
        return max(maxDp)
```



#### [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)[简单]

[1年前，07/14、]

```
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400
```

审题：1、非负；2、不连续

![image-20200714093224936](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200714093224936.png)

![image-20200714093402710](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200714093402710.png)

**dp + 滚动数组**

![image-20200714101108569](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200714101108569.png)

代码：

![image-20200714101225317](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200714101225317.png)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 审题：一夜，不能偷连续房间；非负；return max_sum
        # dp: dp[i] = max((dp[i-2] + nums[i]), dp[i-1])
        # 空间最优，原数组修改
        # time:O(N)
        # space:O(1)
        # 28ms, 99.25%

        nums_len = len(nums)
        if not nums: return 0
        if nums_len == 1: return nums[0]
        # if nums_len == 2: return max(nums[0], nums[1])    # 可以没有
        
        nums[1] = max(nums[0], nums[1])              # error: 别忘了& max(..)
        for i in range(2, nums_len):
            nums[i] = max((nums[i-2] + nums[i]), nums[i-1])

        # 因为全是非负，最后一个值最大！！！
        return nums[-1]
```

二维数组：

![image-20200714100927575](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200714100927575.png)

![image-20200714100903224](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200714100903224.png)





#### [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)[中等]

```
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

审题：

在198的基础上，变成了环，可以拆分成两种情况：含首的和含尾的

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 44ms, 49.56%
        # 以下步骤不能少
        nums_len = len(nums)  
        if not nums: return 0
        if nums_len == 1: return nums[0]
        return max(self.subrob(nums[:-1]), self.subrob(nums[1:]))

    def subrob(self, nums):
        nums_len = len(nums)
        if not nums: return 0
        if nums_len == 1: return nums[0]
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return nums[-1]
```



#### [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)[简单]

```
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```



#### [91. 解码方法](https://leetcode-cn.com/problems/decode-ways/)

```
91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
```

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 审题：输入：非空，str，只有数字0-9，输出：解码总数（int）
        # special：输入非空校验；首字母为0，不行！
        # 一位字符为1-9，就可以解码，0不行
        # 两位字符10-26，可以解码

        # dp[i] 以第i个字符结尾的字符串解码方法总数
        # dp[i] = dp[i-1] + dp[i-2] 有条件的

        if not s: return 0
        if s[0] == "0": return 0

        s_len = len(s)
        dp = [0 for _ in range(s_len)]         # error: dp! not dp[], 0 int型
        dp[0] = 1

        for i in range(1, s_len):
            # 判断1位字符解码：如果当前字符为1-9, 不为0，1位字符可以解码
            if s[i] != "0":                    
                dp[i] = dp[i - 1]

            # 判断两位字符解码：如果10-26，可以解码
            num = 10 * (ord(s[i-1]) - ord("0")) + ord(s[i]) - ord("0")
            if 10 <= num <= 26:                # error: 10
                if i == 1:                     # error: !
                    # 当i为1时，dp[i - 2]不存在，因为要单独写+1
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
    
        return dp[-1]
```



```

不用算术运算的加法——电路中的与或非门
解题思路
根据 a&b 获取不带进位的求和， a^b 获取标记位， 通过标记位左移1位， 进一步和不带进位的结果进行求和与求进位，直至进位为0，结束循环。
```

```python
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
```



#### [221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/)

```
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:
输入: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4
```



**分析：**

**暴力**



**dp**

我们用 dp(i, j)表示以 (i, j) 为右下角，且只包含 1的正方形的边长最大值。

那么如何计算 dp 中的每个元素值呢？对于每个位置 (i, j)，检查在矩阵中该位置的值：

如果该位置的值是 0，则 dp(i, j) = 0，因为当前位置不可能在由 1 组成的正方形中；

如果该位置的值是 1，则 dp(i, j)的值由其上方、左方和左上方的三个相邻位置的 dp 值决定。

**【分类：首行、首例，其他---- 通用】**

1、当前位置的元素值等于三个相邻位置的元素中的最小值加 1，状态转移方程如下：dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1

2、考虑**边界条件**。如果 i 和 j 中至少有一个为 0，则以位置 (i, j) 为右下角的最大正方形的边长只能是 1，因此 dp(i, j) = 1。

![image-20200718112828741](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200718112828741.png)

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 72ms, 85.57%
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])            # 缩进

        return maxSide **2           # error：**2 平方
```

**复杂度分析**

时间复杂度：O(mn)，其中 m 和 n 是矩阵的行数和列数。需要遍历原始矩阵中的每个元素计算 dp 的值。

空间复杂度：O(mn)，其中 m 和 n 是矩阵的行数和列数。创建了一个和原始矩阵大小相同的矩阵 dp。由于状态转移方程中的 dp(i, j)由其上方、左方和左上方的三个相邻位置的 dp值决定，因此可以使用两个一维数组进行状态转移，空间复杂度优化至 O(n)。
链接：https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/

暴力代码：

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    max_side = max(max_side, 1)
                    # 计算可能的最大正方形边长
                    current_max_side = min(rows - i, columns - j)
                    for m in range(1, current_max_side):
                        # 判断新增的一行一列是否均为1
                        flag = True
                        if matrix[i + m][j + m] == "0":
                            break
                        for n in range(m):
                            if matrix[i + m][j + n] == "0" or matrix[i + n][j + m] == "0":
                                flag = False
                                break
                        if flag:
                            max_side = max(max_side, m + 1)
                        else:
                            break
            
        return max_side **2
```

