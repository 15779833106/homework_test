class TreeNode():
    """定义树节点"""

    def __init__(self, data, left=None, right=None):
        """data为树结点存储的数据,left,right为左右子树"""
        self.data = data
        self.left = left
        self.right = right


def isBalanced(root: TreeNode):
    def dfs(node, depth):
        if not node:
            return 0
        l = dfs(node.left, depth + 1)
        r = dfs(node.right, depth + 1)
        return max(l, r) + 1

    if not root:
        return True
    if abs(dfs(root.left, 0) - dfs(root.right, 0)) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


if __name__=="__main__":
    node5=TreeNode(7,None,None)
    node4 = TreeNode(15, None, None)
    node3 = TreeNode(20, node4, node5)
    node2 = TreeNode(9, None, None)
    root = TreeNode(3, node2, node3)

    print(isBalanced(root))