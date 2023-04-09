# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     # 递归方法
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         if head.val == val:
#             return head.next
#         if not head:
#             return None
#         else:
#             head.next = self.deleteNode(head.next, val)
#             return head


class Solution:
    # 双指针
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        now = head.next
        pre = head
        while now:
            if now.val != val:
                now = now.next
                pre = pre.next
            else:
                now = now.next
                pre.next = now
                return head
