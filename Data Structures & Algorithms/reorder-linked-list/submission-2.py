# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now we are at the mid-point
        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse l2
        curr, prev = l2, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev is the new head
        l2 = prev
        # new list
        dummy = ListNode()
        ptr = dummy
        while l1 and l2:
            ptr.next = l1
            l1 = l1.next
            ptr = ptr.next
            ptr.next = l2
            l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        return