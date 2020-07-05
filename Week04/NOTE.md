## 1 敲代码，看代码，改进，持续改进的过程

### 1.1 生成式 [ ]

​		[num for num in range(8)]

```python
>>> [[i] for i in range(10)] 
[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

2、将两个嵌套for循环写成一个列表生成式
如，有一个嵌套列表，a=[[1,2],[3,4],[5,6]]，要提取列表里的每一个元素
用for循环处理：
for i in a:
    for j in i:
        print(j)
>>> [j for i in a for j in i]     # 先写外循环，后写内循环 !!!
[1, 2, 3, 4, 5, 6]
>>> [j for j in i for i in a] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined        # 否则报错：
```

​	https://www.cnblogs.com/heyyw1119/p/8711462.html

[	Python基础知识--Slice（切片）和Comprehensions（生成式）](https://www.cnblogs.com/heyyw1119/p/8711462.html)

### 1.2 max, min, sum

​		max_profit = (max_profit, (profit - min_buy_price))

   	return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

### 1.3 

```python
            elif ten > 0:        # 直接写即可
                # 收一个20美元，两种找零方法：5+10 和 5*3，优先找大额的
                ten -= 1
                five -= 1
            else:
                five -= 3
                
            # elif bill = 20:
            #     # 收一个20美元，两种找零方法：5+10 和 5*3，优先找大额的
            #     if ten > 0:
            #         ten -= 1
            #         five -= 1
            #     else:
            #         five -= 3
            
```



## 2 错误整理

nums[mid]  and mid



## 3 复杂度总结

线性N 

跳跃遍历logN 

傻递归2^N 

排序nlogN



## 4 贪心算法

真实场景：每一步最好，整体不一定最好

因此需要证明：其成立

可以做为辅助算法：最小生成树、



贪心算法：不回退，每一步（子问题）都找到当前状态下，最好或最优的选择，从而得出全局最好或最优的算法

动态规划：回退，保存之前的运算结果，和当前最好的选择，二者比较，择优录取。



贪心：【每一步做出最优判断】

回溯：【回退：清除数据】

动态规划：【每一步做出最优判断  +  回退  =  二者比较，择优录取】



**使用场景:**

从前向后、从后向前

证明可以用贪心



## 5 二分查找

### 模板

```python
# 二分查找

left, right = 0, len(List) - 1
while left <= right:       # <=
    mid = (left + right)//2
    if List[mid] == target:
        # find the target
        break or return result
    elif List[mid] > target:
        right = mid -1
    else:
        left = mid + 1
```

### 适用条件

单调数组（递增或递减） 【否则就只能遍历了】

存在上下界（bounded）【有边界，向中间收缩】

通过索引访问（index accessible ）



## 6 BFS DFS

**DFS：**用递归、栈

recursion

```python
visited = set()

def dfs(node, visited):
    if node in visited:    # terminator
        # already visited
        return 

    visited.add(node)

    # process current node here.
    ...
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)
```

stack

```python
def DFS(self, tree):
    if tree.root is None:
        return []

    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

    # other processing work
    ...
```

**BFS：**用队列

```python
# BFS
def BFS(graph, start, end):
    visited = set()
    queue = []
    queue.append([start])

    while queue:
        node = queue.pop()
        visited.add(node)

        processs(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing word
    ...
```

