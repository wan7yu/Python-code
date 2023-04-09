"""
AVL树
1.空二叉树是一个 AVL 树
2.如果 T 是一棵 AVL 树，那么其左右子树也是 AVL 树，并且 |h(ls)-h(rs)|<=1，h 是其左右子树的高度
3.树高为 logn
平衡因子：右子树高度 - 左子树高度

使用二叉搜索树的目的之一是缩短插入与查找时间，一棵合理的二叉搜索树插入与查找时间可以缩短到O(logn)。

对于一般的二叉搜索树，有可能退化为链表。想象一棵每个结点只有右孩子的二叉搜索树，
那么它的性质就和链表一样，插入与查找时间都是O(n)，可以说是极大的时间浪费，所以研究平衡二叉搜索树是非常有必要的。

关于查找效率分析，如果树的高度为 h，则在最坏的情况，查找一个关键字需要对比 h 次，
查找时间复杂度（也为平均查找长度 ASL，Average Search Length）不超过O(h)。

二叉搜索树的「平衡」概念是指：每一个结点的左子树和右子树高度差最多为 1。

ALV树可以对不平衡时的情况进行调整，使不平衡的二叉搜索树变得平衡。
"""


class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.lchild = None
        self.rchild = None
        self.high = 0


class AVLTree:
    def __init__(self, li=None) -> None:
        self.root = None
        if li:
            for val in li:
                self.root = self.insert(self.root, val)

    def high(self, node):
        """获取深度"""
        """
        利用深度计算平衡因子，以及树的高度
        """
        if not node:
            return -1
        else:
            return node.high

    def preorder(self, node):
        """先序遍历"""
        if not node:
            return
        print(node.data, end=',')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if not node:
            return
        self.inorder(node.lchild)
        print(node.data, end=',')
        self.inorder(node.rchild)

    def postorder(self, node):
        """后续遍历"""
        if not node:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.data, end=',')

    def find_max(self, node):
        """求最大值结点"""
        if not self.root:
            raise ValueError("The AVL tree is null")
        if node.rchild:
            return self.find_max(node.rchild)
        else:
            return node

    def find_min(self, node):
        """求最小值结点"""
        if not self.root:
            raise ValueError("The AVL tree is null")
        if node.lchild:
            return self.find_min(node.lchild)
        else:
            return node

    def query(self, node, val):
        """递归查询方法"""
        if not node:
            return None
        if node.data > val:
            return self.query(node.lchild, val)
        elif node.data < val:
            return self.query(node.rchild, val)
        else:
            return node

    def query_no_rec(self, val):
        """非递归查询方法"""
        p = self.root
        while p:
            if p.data > val:
                p = p.lchild
            elif p.data < val:
                p = p.rchild
            else:
                return p
        else:
            raise KeyError("Error, value  not in the tree")

    def rotate_RR(self, node):
        """节点的右孩子的右子树插入元素导致的左旋"""
        new_node = node.rchild
        node.rchild = new_node.lchild
        new_node.lchild = node
        node.high = max(self.high(node.lchild), self.high(node.rchild))+1
        new_node.high = max(self.high(new_node.rchild), node.high)+1
        return new_node

    def rotate_LL(self, node):
        """节点的左孩子的左子树插入元素导致的右旋"""
        new_node = node.lchild
        node.lchild = new_node.rchild
        new_node.rchild = node
        node.high = max(self.high(node.lchild), self.high(node.rchild))+1
        new_node.high = max(self.high(new_node.lchild), node.high)+1
        return new_node

    def rotate_LR(self, node):
        """节点的左孩子的右子树的插入导致的先左再右旋"""
        node.lchild = self.rotate_RR(node.lchild)
        new_node = self.rotate_LL(node)
        return new_node

    def rotate_RL(self, node):
        """节点的右孩子的左子树的插入导致的先左再右旋"""
        node.rchild = self.rotate_LL(node.rchild)
        new_node = self.rotate_RR(node)
        return new_node

    def insert(self, node, val):
        """递归插入方法"""
        # 根节点特殊处理
        if not self.root:
            self.root = AVLNode(val)
            return self.root
        # 普通节点处理
        if not node:
            node = AVLNode(val)
            return node
        # 左孩子两种插入情况
        if val < node.data:
            node.lchild = self.insert(node.lchild, val)
            if (self.high(node.lchild)-self.high(node.rchild)) == 2:
                # 左孩子左子树，右旋
                if val < node.lchild.data:
                    node = self.rotate_LL(node)
                # 左孩子右子树，左旋再右旋
                else:
                    node = self.rotate_LR(node)
            # 重新计算高度
            node.high = max(self.high(node.lchild), self.high(node.rchild))+1
            return node
        # 右孩子两种插入情况
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            if (self.high(node.rchild)-self.high(node.lchild)) == 2:
                # 右孩子右子树，左旋
                if val > node.rchild.data:
                    node = self.rotate_RR(node)
                # 右孩子左子树，右旋再左旋
                else:
                    node = self.rotate_RL(node)
            # 重新计算高度
            node.high = max(self.high(node.lchild), self.high(node.rchild))+1
            return node

    def delete(self, val):
        """删除方法"""
        # 从root往后找
        self.root = self.remove(self.root, val)

    def remove(self, node, val):
        """具体删除情况"""
        if node is None:
            print("the value not in tree")
            return None
        # 删除的值是当前节点的左孩子
        elif val < node.data:
            node.lchild = self.remove(node.lchild, val)
            if (self.high(node.rchild)-self.high(node.lchild)) == 2:
                if self.high(node.rchild.rchild) >= self.high(node.rchild.lchild):
                    node = self.rotate_RR(node)
                else:
                    node = self.rotate_RL(node)
            node.high = max(self.high(node.lchild),
                            self.high(node.rchild))+1
        # 删除的值是当前节点的右孩子
        elif val > node.data:
            node.rchild = self.remove(node.rchild, val)
            if (self.high(node.lchild)-self.high(node.rchild)) == 2:
                if self.high(node.lchild.lchild) >= self.high(node.lchild.rchild):
                    node = self.rotate_LL(node)
                else:
                    node = self.rotate_LR(node)
            node.high = max(self.high(node.lchild),
                            self.high(node.rchild))+1
        # 删除的节点是当前节点
        else:
            # 当前节点有左右孩子
            if node.lchild and node.rchild:
                if node.lchild.high <= node.rchild.high:
                    minNode = self.find_min(node.rchild)
                    node.data = minNode.data
                    node.rchild = self.remove(node.rchild, node.data)
                else:
                    maxNode = self.find_max(node.lchild)
                    node.data = maxNode.data
                    node.lchild = self.remove(node.lchild, node.data)
                node.high = max(self.high(node.lchild),
                                self.high(node.rchild))+1
            # 当前节点只有左孩子或者右孩子
            elif node.rchild:
                node = node.rchild
            elif node.lchild:
                node = node.lchild
            # 当前节点是叶子节点
            else:
                node = None

        return node

    def printTravel(self, node):
        """打印函数"""
        print("先序遍历: ", end="")
        self.preorder(node)
        print('\n')
        print("中序遍历: ", end="")
        self.inorder(node)
        print('\n')
        print("后序遍历: ", end="")
        self.postorder(node)
        print('\n')


li = [68, 38, 76, 11, 42, 22, 69, 85, 70, 79, 98, 9]


tree = AVLTree(li)
print("the original list :", li)
tree.printTravel(tree.root)
tree.delete(98)
tree.delete(79)
tree.delete(69)
# x = int(input("请输入要删除的值:"))
# tree.delete(x)
tree.printTravel(tree.root)
