# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     """反转链表方法"""
#     # (self, l1:Optiona[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#     def addTwoNumbers(self, l1):
#         # 定义进位
#         carry = 0
#         l1, l2 = self.reverse(l1), self.reverse(l2)
#         # 指针
#         p1, p2 = l1, l2
#         """位数相同时的情况在while里面就已经解决"""
#         while p1 and p2:
#             # 每次求和前先计算进位
#             carry = (p1.val + p2.val) // 10
#             # 进位为1,取余
#             """这里解决了要进位时，p1的情况
#             此时p1一定不会比p2小(小的话创建)
#             """
#             if carry:
#                 # 把求和后的值对10求余，赋给新l1
#                 p1.val = (p1.val + p2.val) % 10
#                 # 判断后继是否存在
#                 if p1.next:
#                     # 存在后继，值加一
#                     p1.next.val += carry
#                 else:
#                     # 否则创建一个值为1的新节点
#                     p1.next = ListNode(carry)
#             # 进位为0，直接相加
#             else:
#                 p1.val = p1.val + p2.val
#                 """这里解决当不用进位时，p1比p2位数小的情况
#                 因为将l1作为新结点使用，如果p1比p2位数小时
#                 要将l1的最后一个结点与l2连接。
#                 例如:  l1: 12
#                        l2: 233
#                 这时候要将353返回，就需要连接最后一个新l1的5和l2的3
#                 """
#                 if not p1.next and p2.next:
#                     p1.next = p2.next
#                     break
#             p1 = p1.next
#             p2 = p2.next
#         """当p2位数比p1小时，计算p1的值是不是要进位"""
#         while p1:
#             carry = p1.val // 10
#             if carry:
#                 p1.val = p1.val % 10
#                 if p1.next:
#                     p1.next.val += carry
#                 else:
#                     p1.next = ListNode(carry)
#                 p1 = p1.next
#             # 如果不用进位，则后面的数都不用进位
#             else:
#                 break
#         return self.reverse(l1)

#     def reverse(self, node: ListNode) -> ListNode:
#         # 反转链表方法
#         cur, pre = node, None
#         while cur:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre

class Solution:
    # 栈
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        ans = None
        while stack1 or stack2 or carry != 0:
            a1 = 0 if not stack1 else stack1.pop()
            b1 = 0 if not stack2 else stack2.pop()
            cur = a1 + b1 + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans
