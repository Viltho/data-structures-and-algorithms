# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = [], []
        if headA is None or headB is None:
            return None
        current = headA
        currentwo = headB
        while current.next is not None:
            a.append(current.val)
            current = current.next
        while currentwo.next is not None:
            b.append(currentwo.val)
            currentwo = currentwo.next