# 回溯 前置知识 二叉树 深度优先算法 递归；
"""
dfs通常使用递归实现，但也可以使用栈来实现。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if not node:
        return
    print(node.val)
    dfs(node.left)
    dfs(node.right)

# 创建一个二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 使用DFS遍历二叉树
dfs(root)
