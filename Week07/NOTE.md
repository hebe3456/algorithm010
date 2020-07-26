![image-20200724101337721](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200724101337721.png)

#### Trie树理论

![image-20200724101620805](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200724101620805.png)

![image-20200724101740662](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200724101740662.png)

![image-20200724101959980](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200724101959980.png)

![image-20200724102059615](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200724102059615.png)



Trie 树优于哈希表的另一个理由是，随着哈希表大小增加，会出现大量的冲突，时间复杂度可能增加到 O(n)，其中 n是插入的键的数量。与哈希表相比，Trie 树在存储多个具有相同前缀的键时可以使用较少的空间。此时 Trie 树只需要 O(m)的时间复杂度，其中 m 为键长。而在平衡树中查找键值需要 O(mlogn) 时间复杂度。

应用：

1. 自动补全，eg:  谷歌的搜索建议

2. 拼写检查,   eg:  文字处理软件中的拼写检查

3. IP 路由 (最长前缀匹配),  eg:  使用Trie树的最长前缀匹配算法，Internet 协议（IP）路由中利用转发表选择路径。

4. T9 (九宫格) 打字预测,   eg:  T9（九宫格输入），在 20 世纪 90 年代常用于手机输入

5. 单词游戏,   eg:  Trie 树可通过剪枝搜索空间



![image-20200725101845954](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200725101845954.png)



#### 并查集 

![image-20200726190851020](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200726190851020.png)

![image-20200725101230990](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200725101230990.png<img src="C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200725101211828.png" style="zoom:33%;" />



![image-20200725103138542](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200725103138542.png)





![image-20200725104510761](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200725104510761.png)





AVL 和红黑树

![image-20200726201312875](C:\Users\RL\AppData\Roaming\Typora\typora-user-images\image-20200726201312875.png)

四种旋转，和为什么引入旋转