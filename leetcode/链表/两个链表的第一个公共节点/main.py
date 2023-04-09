"""
双指针法
(浪漫相遇)
我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，然后同时分别逐结点遍历，
当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；
当 node2 到达链表 headB 的末尾时，重新定位到链表 headA 的头结点。

这样，当它们相遇时，所指向的结点就是第一个公共结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        pre1, pre2 = headA, headB
        while pre1 != pre2:
            if pre1:
                pre1 = pre1.next
            else:
                pre1 = headB
            if pre2:
                pre2 = pre2.next
            else:
                pre2 = headA
        return pre1


# class Solution:
#     """哈希表方法(不推荐)"""

#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB:
#             return
#         hashlist = []
#         tmp = headA
#         while tmp:
#             hashlist.append(tmp)
#             tmp = tmp.next
#         tmp = headB
#         while tmp:
#             if tmp in hashlist:
#                 return tmp
#             tmp = tmp.next
#         else:
#             return None
