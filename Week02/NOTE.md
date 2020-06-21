学习笔记

这周有点儿忙，
主要是就是想办法节约时间：

1 抓主要矛盾，找最好的最重要的代码去记，去理解，细枝末节该放就放。

第五课   哈希表、映射、集合

Hash table
哈希表（Hash table），也叫散列表，是根据关键码值（Key value）而直接进行访问的数据结构
Python中称为字典 dict

作用：加快查找的速度（通过把关键码值映射到表中一个位置来访问记录）

映射函数叫作散列函数（Hash Function），存放记录的数组 叫作哈希表（或散列表）

工程实践
• 电话号码簿
• 用户信息表
• 缓存（LRU Cache）  。。。
• 键值对存储（Redis）


第六课  树、二叉树、二叉搜索

Linked List是特殊的Tree (一个儿子)
Tree 是特殊的 Graph     (没有环)

节点定义代码：

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
		
 public class TreeNode {
     public int val;
     public TreeNode left, right;
     public TreeNode(int val) {
         this.val = val;
         this.left = null;
         this.right = null;
     }
 }

二叉树遍历 Pre-order/In-order/Post-order
1.前序（Pre-order）：根-左-右
2.中序（In-order）：左-根-右
3.后序（Post-order）：左-右-根

二叉树的前中后序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

前：
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        traverse_path = []
        self.preorder(root, traverse_path)
        return traverse_path

    def preorder(self, root, traverse_path):
        if root:
            traverse_path.append(root.val)
            self.preorder(root.left, traverse_path)
            self.preorder(root.right, traverse_path)


后：
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        traverse_path = []
        self.postorder(root, traverse_path)
        return traverse_path

    def postorder(self, root, traverse_path):
        if root:
            self.postorder(root.left, traverse_path)
            self.postorder(root.right, traverse_path)
            traverse_path.append(root.val)

中：
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traverse_path = []
        self.inorder(root, traverse_path)
        return traverse_path

    def inorder(self, root, traverse_path):
        if root:
            self.inorder(root.left, traverse_path)
            traverse_path.append(root.val)
            self.inorder(root.right, traverse_path)
推荐使用递归，和迭代速度差不多，推荐递归！！！


二叉搜索树 Binary Search Tree
二叉搜索树，也称二叉搜索树、有序二叉树（Ordered Binary Tree）、 排序二叉树（Sorted Binary Tree），
是指一棵空树或者具有下列性质的二叉树：  ！！！
1. 左子树上所有结点的值均小于它的根结点的值； 
2. 右子树上所有结点的值均大于它的根结点的值； 
3. 以此类推：左、右子树也分别为二叉搜索树。 （这就是重复性！）
中序遍历：升序排列

二叉搜索树常见操作   
1. 查询
2. 插入新结点（创建）
3. 删除
time: average: O(logN), worst:O(N)
