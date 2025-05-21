"""
Problem: Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            if fast is None:
                return head  # n is larger than the length of the list
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            if slow is None or slow.next is None:
                return dummy.next
            slow = slow.next
        if slow and slow.next:
            slow.next = slow.next.next
        return dummy.next
