# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 辅助栈方法
    # 时间复杂度O(n),空间复杂度O(n)
    def reversePrint(self, head: ListNode) -> list[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


# class Solution:
#     # 递归方法
#     def reversePrint(self, head: ListNode) -> list[int]:
#         if head:
#             return self.reversePrint(head.next)+[head.val]
#         else:
#             return []
