class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def longestpath(self, root=None):
        ans = 0

        def dfs(root, parent_val):
            nonlocal ans
            if not root:
                return 0
            l = dfs(root.left, root.val)
            r = dfs(root.right, root.val)
            ans = max(ans, l + r)
            if root.val != parent_val:
                return 0
            return max(l, r) + 1

        if not root:
            return ans
        dfs(root, root.val)
        return ans

node6=TreeNode(5)
node5=TreeNode(1)
node4=TreeNode(1)
node3=TreeNode(5,left=None,right=node6)
node2=TreeNode(4,node5,node4)
node1=TreeNode(5,node2,node3)
s=Solution().longestpath(node1)
print(s)
