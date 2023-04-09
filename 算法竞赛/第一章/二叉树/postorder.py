"""
已知前序和中序求后序
"""


# class TreeNode:
#     def __init__(self, val=0, lchild=None, rchild=None) -> None:
#         self.val = val
#         self.lchild = lchild
#         self.rchild = rchild


# class Solution:
#     def recreate_tree(self, inorder, preorder):
#         if not preorder:
#             return
#         root = TreeNode(preorder[0])
#         idx = 0
#         for i in range(len(inorder)):
#             if inorder[i] == root.val:
#                 idx = i
#                 break
#         root.lchild = self.recreate_tree(inorder[:idx], preorder[1:idx+1])
#         root.rchild = self.recreate_tree(inorder[idx+1:], preorder[idx+1:])
#         return root

#     def postorder(self, root):
#         if root:
#             self.postorder(root.lchild)
#             self.postorder(root.rchild)
#             print(root.val, end=' ')


# s = Solution()
# preorder = ['G', 'D', 'A', 'F', 'E', 'M', 'H', 'Z']
# inorder = ['A', 'D', 'E', 'F', 'G', 'H', 'M', 'Z']
# root = s.recreate_tree(inorder, preorder)
# s.postorder(root)
class TreeNode():
    def __init__(self, val=0, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild


class Solution():
    def recreate(self, postorder, inorder):
        if not postorder:
            return
        root = TreeNode(postorder[-1])
        idx = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                idx = i
                break
        root.lchild = self.recreate(postorder[:idx], inorder[:idx])
        root.rchild = self.recreate(
            postorder[idx:-1], inorder[idx+1:])
        return root

    def preorder(self, root):
        if root:
            print(root.val, end='')
            self.preorder(root.lchild)
            self.preorder(root.rchild)


s = Solution()
inorder = input().strip()
postorder = input().strip()
root = s.recreate(postorder, inorder)
s.preorder(root)
