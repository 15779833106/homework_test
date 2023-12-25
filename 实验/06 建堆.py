def buildmaxheap(lst):
    length=len(lst)
    i=length//2
    lst.insert(0,0)
    while i>=1:
        heapify(lst,i)
        i=i-1
    lst.pop(0)
    return lst


def heapify(temp, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left <=len(temp)-1 and temp[left] > temp[largest]:
        largest = left
    if right <=len(temp)-1 and temp[right] > temp[largest]:
        largest = right

    if largest != i:
        temp[i], temp[largest] = temp[largest], temp[i]
        heapify(temp, largest)

class TreeNode():
    """定义树节点"""
    def __init__(self,data,left=None,right=None):
        """data为树结点存储的数据,left,right为左右子树"""
        self.data=data
        self.left=left
        self.right=right

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

    def isComplete(self):
        if self.root==None:
            return True
        isLeaf=False
        queue=[]
        queue.append(self.root)
        while queue:
            root=queue.pop(0)
            left=root.left
            right=root.right
            if (not left and right) or (isLeaf and (left or right)):
                return False
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            if not left or not right:
                isLeaf=True
        return True


def heapsort(lst):
    arr=[]
    buildmaxheap(lst).insert(0,0)
    i=len(lst)-1
    while i>=1:
        lst[1],lst[i]=lst[i],lst[1]
        a=lst.pop()
        arr.append(a)
        heapify(lst,1)
        i=i-1
    return arr

tree=BinTree()

for i in buildmaxheap([80,40,30,60,81,90,100,10]):
    tree.add(i)

print(tree.isComplete())

print(buildmaxheap([80,40,30,60,81,90,100,10]))
print(heapsort([80,40,30,60,81,90,100,10]))