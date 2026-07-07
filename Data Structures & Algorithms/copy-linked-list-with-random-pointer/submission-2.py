"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}
        curr = head
        while curr:
            nodes[curr] = Node(curr.val, curr.next, None)
            curr = curr.next
        dummy = Node(0)
        # dummy.next = head
        p1 = head
        p2 = dummy
        while p1:
            p2.next = nodes[p1]
            nodes[p1].random = nodes[p1.random]
            p1 = p1.next
            p2 = p2.next
        return dummy.next