#结点
class TreeNode():
    """定义树节点"""
    def __init__(self,data,left=None,right=None):
        """data为树结点存储的数据,left,right为左右子树"""
        self.data=data
        self.left=left
        self.right=right


#二叉树
class BinTree():
    """创建二叉树"""
    def __init__(self):
        '''定义初始化函数'''
        self.root=None    #初始化根节点为None
        self.ls=[]       #定义列表用于存储结点地址

    def add(self,data):
        '''定义add方法，向树结构中添加元素'''
        node=TreeNode(data)   #实例化树节点
        if self.root==None:   #若根节点为None，添加根节点，并将根节点地址值添加到self.ls中
            self.root=node
            self.ls.append(self.root)
        else:
            rootNode=self.ls[0]   #将第一个元素设为根节点
            if rootNode.left==None:  #若根节点的左子树为空，添加左节点，并将地址值添加到self.ls中
                rootNode.left=node
                self.ls.append(rootNode.left)
            elif rootNode.right==None:  #若根节点的右子树为空，添加右节点，并将地址值添加到self.ls中
                rootNode.right=node
                self.ls.append(rootNode.right)
                self.ls.pop(0)   #弹出self.ls第一个位置的元素

    def preOrderTraversal(self,root):
        '''前序遍历'''
        if root==None:
            return
        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def preOrderStack(self,root):
        '''前序遍历，堆栈'''
        if root==None:
            return
        stack=[]
        result=[]
        node=root
        while node or stack:
            while node:
                result.append(node.data)
                stack.append(node)
                node=node.left
            node=stack.pop()
            node=node.right
        print(result)

    def inOrderTraversal(self,root):
        '''中序遍历'''
        if root==None:
            return
        self.inOrderTraversal(root.left)
        print(root.data)
        self.preOrderTraversal(root.right)

    def inOrderStack(self,root):
        '''中序遍历'''
        if root==None:
            return
        stack=[]
        result=[]
        node=root
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            result.append(node.data)
            node=node.right
        print(result)

    def postOrderTraversal(self,root):
        '''后续遍历'''
        if root==None:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data)

    def postOrderStack(self,root):
        '''后序遍历'''
        if root==None:
            return
        stack=[]
        seq=[]
        result=[]
        node=root
        while node or stack:
            while node:
                seq.append(node.data)  #将扫描到的元素放入seq中
                stack.append(node)     #栈内添加结点
                node=node.right       #
            node=stack.pop()
            node=node.left
        while seq:
            result.append(seq.pop())
        print(result)



if __name__=='__main__':
    tree=BinTree()  #实例化二叉树
    for i in range(1,11):
        tree.add(i)
    print(tree.preOrderTraversal(tree.root))

