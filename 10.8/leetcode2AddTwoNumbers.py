# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = 0
        val2 = 0
        i = 1

        while l1:
            val1 = val1 + l1.val * i
            i = i * 10
            l1 = l1.next

        i = 1
        while l2:
            val2 = val2 + l2.val * i
            i = i * 10
            l2 = l2.next

        val3 = str(val1 + val2)
        for tmp in val3:
            cur = ListNode(int(tmp))
            if not head:
                head = cur
            else:
                cur.next = head
                head = cur
        return head