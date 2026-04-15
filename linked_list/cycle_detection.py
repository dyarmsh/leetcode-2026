from typing import Optional

"""
[MEDIUM] REMOVE NTH NODE FROM END OF LINKED LIST
https://neetcode.io/problems/remove-node-from-end-of-linked-list/

Date: 15th Apr 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len of linked list
Space: O(1)
    - no extra memory consumed by using slow and fast pointers
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    
    # Time: O(n), Space: O(1)
    slow = head
    fast = head

    while head: 
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

    
    # Time: O(n), Space: O(n)
    nodes = set()

    while head:

        if head in nodes:
            return True
            
        nodes.add(head)  
        head = head.next

    return False
        