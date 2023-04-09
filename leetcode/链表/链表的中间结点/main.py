"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """方法一:遍历求长度"""

    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        count = 0
        while p1:
            count += 1
            p1 = p1.next
        for i in range(count // 2):
            head = head.next
        return head


class Solution:
    """快慢指针(双指针)"""

    def middleNode(self, head: ListNode) -> ListNode:
        low, fast = head, head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low
