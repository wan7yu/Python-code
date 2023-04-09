# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义进位
        carry = 0
        # 指针
        p1, p2 = l1, l2
        """位数相同时的情况在while里面就已经解决"""
        while p1 and p2:
            # 每次求和前先计算进位
            carry = (p1.val + p2.val) // 10
            # 进位为1
            """这里解决了要进位时p1的情况"""
            if carry:
                # 把求和后的值对10求余，赋给新l1
                p1.val = (p1.val + p2.val) % 10
                # 判断后继是否存在
                if p1.next:
                    # 存在后继，值加一
                    p1.next.val += carry
                else:
                    # 否则创建一个值为1的新节点
                    p1.next = ListNode(carry)
            # 进位为0
            else:
                # 直接相加
                p1.val = p1.val + p2.val
                """这里解决当不用进位时，p1比p2位数小的情况
                因为将l1作为新结点使用，如果p1比p2位数小时
                要将l1的最后一个结点与l2连接。
                例如:  l1: 12
                       l2: 233
                这时候要将353返回，就需要连接最后一个新l1的5和l2的3
                """
                if not p1.next and p2.next:
                    p1.next = p2.next
                    break
            p1 = p1.next
            p2 = p2.next
        """当p2位数比p1小时，计算p1的值是不是要进位"""
        while p1:
            carry = p1.val // 10
            if carry:
                p1.val = p1.val % 10
                if p1.next:
                    p1.next.val += carry
                else:
                    p1.next = ListNode(carry)
                p1 = p1.next
            # 如果不用进位，则后面的数都不用进位
            else:
                break
        return l1
