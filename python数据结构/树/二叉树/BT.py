"""
建立一棵二叉树， 并对其进行深度优先遍历（先序、中序、后序）
广度优先遍历（层次遍历）打印输出遍历结果。
"""


class Node(object):
    """ 节点类 """

    def __init__(self, value=None, lchild=None, rchild=None):
        # 节点权值 以及 左、右孩子
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class Binary_Tree(object):
    """ 二叉树类 """

    def __init__(self, root=None):
        self.root = root

    # 定义创建二叉树方法
    def create(self, list=None):
        # 传入一个列表
        if not list:
            return
        # 利用列表来存放所有节点
        tmp = []
        for i in list:
            if i == None:
                tmp.append(None)
            else:
                tmp.append(Node(i))
        # 头节点为第一个元素
        self.root = tmp[0]
        # 对于二叉树，深度为结点数除以二减一
        for idx in range(len(list)//2):
            # 如果左孩子没超过最大深度，并且不为空
            if idx * 2 + 1 < len(tmp) and tmp[idx * 2 + 1]:
                tmp[idx].lchild = tmp[idx * 2 + 1]
            if idx * 2 + 2 < len(tmp) and tmp[idx * 2 + 2]:
                tmp[idx].rchild = tmp[idx * 2 + 2]

    # 深度优先遍历：先序遍历---根 左 右
    def preorder(self, node):
        """递归实现先序遍历"""
        # 判断是否为空树
        if not node:
            return
        # 输出元素，递归输出左、右子树
        print(node.value, end=',')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    # 深度优先遍历：中序遍历---左 根 右
    def inorder(self, node):
        """递归实现中序遍历"""
        if not node:
            return
        # 输出的是第二次访问的节点
        self.inorder(node.lchild)
        print(node.value, end=',')
        self.inorder(node.rchild)

    # 深度优先遍历：后序遍历---左 右 根
    def postorder(self, node):
        """递归实现后序遍历"""
        if not node:
            return
        # 输出的是第三次访问的节点
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.value, end=',')

    # 广度优先遍历:层次遍历
    def level(self, node):
        """队列实现层次遍历"""
        if not node:
            return
        queue = []
        queue.append(node)
        # 先进的先出
        while queue:
            tmp = queue.pop(0)
            if not tmp:
                return
            print(tmp.value, end=',')
            queue.append(tmp.lchild)
            queue.append(tmp.rchild)

    def printTravel(self, node):
        print("先序遍历: ", end="")
        self.preorder(node)
        print('\n')
        print("中序遍历: ", end="")
        self.inorder(node)
        print('\n')
        print("后序遍历: ", end="")
        self.postorder(node)
        print('\n')
        print("层次遍历: ", end="")
        self.level(node)


list1 = input("请输入一个二叉树列表:")
binary_tree = Binary_Tree()
binary_tree.create(list1)
binary_tree.printTravel(binary_tree.root)
