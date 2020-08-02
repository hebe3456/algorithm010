#### [1122. 数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/) [简单]

给你两个数组，`arr1` 和 `arr2`，

- `arr2` 中的元素各不相同
- `arr2` 中的每个元素都出现在 `arr1` 中

对 `arr1` 中的元素进行排序，使 `arr1` 中项的相对顺序和 `arr2` 中的相对顺序相同。未在 `arr2` 中出现过的元素需要按照升序放在 `arr1` 的末尾。

**示例：**

```
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
```

 **提示：**

- `arr1.length, arr2.length <= 1000`
- `0 <= arr1[i], arr2[i] <= 1000`
- `arr2` 中的元素 `arr2[i]` 各不相同
- `arr2` 中的每个元素 `arr2[i]` 都出现在 `arr1` 中



```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 1.将arr1的元素统计
        # 2.遍历arr2来提取arr1的元素，将遍历后的元素从arr1中删除
        # 3.剩下的arr1进行排序

        #将arr1 counter计数，按照arr2来取
        li = []
        counter = collections.Counter
        count = counter(arr1)

        #按照arr2将arr1的元素存入li
        for num in arr2:
            if num in count:
                l = count[num]
                for i in range(l):
                    li.append(num)
            #被存的元素删除掉
            del count[num]

        #剩下的元素排序放到末尾
        li += sorted(list(count.elements()))
        return li
```





#### [231. 2的幂](https://leetcode-cn.com/problems/power-of-two/)【简单】

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

**示例 1:**

```
输入: 1
输出: true
解释: 20 = 1
```

**示例 2:**

```
输入: 16
输出: true
解释: 24 = 16
```

**示例 3:**

```
输入: 218
输出: false
```

分析：有且仅有一个二进制位是1

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and (n & (n - 1)) == 0
```

