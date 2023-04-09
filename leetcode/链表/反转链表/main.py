# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     # 辅助栈方法
#     # 时间复杂度O(n),空间复杂度O(n)
#     def reverseList(self, head: ListNode) -> ListNode:
#         stack = []
#         cur = head
#         tmp = head
#         while cur:
#             stack.append(cur.val)
#             cur = cur.next
#         while tmp:
#             tmp.val = stack.pop()
#             tmp = tmp.next
#         return head

# class Solution:
#     # 递归法
#     """将反转链表这个问题看成两个小问题
#     问题1.反转头节点后面的节点
#     问题2.反转头节点
#     假设问题1已经解决,则新的头节点为这个节点既:Node = self.reverseList(head.next)
#     然后把这个新头节点的next指向原来的头节点既:head.next.next = head
#     再把原来头节点的next变为空，既原来头节点变成尾节点:head.next = None
#     递归的终止条件就是：这两个节点都为空既:if not head or not head.next
#     这个时候直接返回头节点即可
#     """

#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         node = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return node


class Solution:
    # 迭代法
    # 时间复杂度O(n),空间复杂度 1
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
