"""
二叉搜索树（又：二叉查找树，二叉排序树，Binary Search Tree，BST）是一种二叉树，
其中每个结点最多有两个子结点且具有二叉搜索树性质：
左子树上所有结点的值均小于它的根结点的值以及右子树上所有结点的值均大于它的根结点的值
"""

import random


class BiTreeNode:
    """ 二叉树结点 """

    def __init__(self, data) -> None:
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    """二叉搜索树"""

    def __init__(self, li=None) -> None:
        """初始化方法，列表赋值"""
        self.root = None
        # 非递归插入方法
        # if li:
        #     for val in li:
        #         self.insert_no_rec(val)
        # 递归插入方法
        if li:
            for val in li:
                self.insert(self.root, val)

    def insert(self, node, val):
        """递归插入方法"""
        # 根节点特殊处理
        if not self.root:
            self.root = BiTreeNode(val)
            return
        # 普通节点处理
        if not node:
            node = BiTreeNode(val)
            return node
        if val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
            return node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
            return node
        else:
            return

    def insert_no_rec(self, val):
        """非递归插入方法"""
        if not self.root:
            self.root = BiTreeNode(val)
            return
        tmp = self.root
        while True:
            # 插入值小于父亲节点
            if val < tmp.data:
                # 左孩子存在，变为左孩子
                if tmp.lchild:
                    tmp = tmp.lchild
                # 否则，创建结点
                else:
                    tmp.lchild = BiTreeNode(val)
                    tmp.lchild.parent = tmp
                    return
            # 插入值大于父亲节点
            elif val > tmp.data:
                if tmp.rchild:
                    tmp = tmp.rchild
                else:
                    tmp.rchild = BiTreeNode(val)
                    tmp.rchild.parent = tmp
                    return
            else:
                return

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

    def __remove_node_1(self, node):
        """node是叶子节点"""
        if not node.parent:
            # 根节点
            self.root = None
        if node == node.parent.lchild:
            # 左孩子
            node.parent.lchild = None
        else:
            # 右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        """node只有一个左孩子"""
        if not node.parent:
            # node的左孩子当根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            # node的左孩子成为父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            # node的左孩子成为父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        """node只有一个右孩子"""
        if not node.parent:
            # node的右孩子当根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            # node的右孩子成为父亲的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            # node的右孩子成为父亲的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        """node有左右孩子"""
        if self.root:
            # 不为空树
            node = self.query_no_rec(val)
            if not node:
                # 无这个值
                return False
            if not node.lchild and not node.rchild:
                # node是叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:
                # node有左孩子
                self.__remove_node_21(node)
            elif not node.lchild:
                # node有右孩子
                self.__remove_node_22(node)
            else:
                # node有左右孩子
                min_node = node.rchild
                # 找到node的右子树中最小的左孩子
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


li = [39, 35, 46, 27, 2, 1, 45, 43, 41, 74, 65, 84, 62, 70, 67, 68, 88]
# random.shuffle(li)

tree = BST(li)
# print("先序遍历")
# tree.preorder(tree.root)
# print()
# print("中序遍历")
# tree.inorder(tree.root)
# print()
# print("后序遍历")
# tree.postorder(tree.root)
# print()
# # print("查找的值为", tree.query(tree.root, 4).data)
# print("查找的值为", tree.query_no_rec(4).data)
print("中序遍历")
tree.inorder(tree.root)
print()
tree.delete(65)
# print(tree.query_no_rec(68).parent == tree.query_no_rec(70))
print("中序遍历")
tree.inorder(tree.root)
print()
