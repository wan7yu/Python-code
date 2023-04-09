# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 双指针
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        if k == 0 or not head:
            return None
        for i in range(k):
            latter = latter.next
        while latter:
            former = former.next
            latter = latter.next
        return former


# class Solution:
#     # 求出长度再遍历
#     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
#         # 当头节点为空时
#         if not head or k == 0:
#             return None
#         cir = head
#         count = 0
#         while cir:
#             count += 1
#             cir = cir.next
#         # 当k大于链表长度时，原样返回
#         if count < k:
#             return head
#         for i in range((count-k)):
#             head = head.next
#         return head
