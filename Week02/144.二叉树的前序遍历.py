#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursively
        # 40ms
        ans = []
        self.dfs(root, ans)
        return ans
    
    def dfs(self, root, ans):
        if root:
            ans.append(root.val)
            self.dfs(root.left, ans)
            self.dfs(root.right, ans)


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 36ms 
        # iteratively
        if not root: return []     # []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
            if node.right:
                stack.append(node.right)    # 后进先出
            if node.left:
                stack.append(node.left)
        return ans


# @lc code=end

