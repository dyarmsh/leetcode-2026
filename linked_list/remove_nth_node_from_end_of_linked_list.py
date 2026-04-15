from typing import Optional

"""
[MEDIUM] REMOVE NTH NODE FROM END OF LINKED LIST
https://neetcode.io/problems/remove-node-from-end-of-linked-list/

Date: 15th Apr 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len of linked list
Space: O(1)
    - node removed from original linked list
    - no extra memory consumed
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    node = head

    # 1st pass: calculate length of linked list
    length = 0
    while node:
        length += 1
        node = node.next

    # 2nd pass: go to nth last node to remove it
    idx_to_remove = length - n
    curr_idx = 0

    node = head
    prev = dummy

    while node:
        if curr_idx == idx_to_remove:
            prev.next = node.next
            break
        curr_idx += 1
        prev = node
        node = node.next

    return dummy.next
        
        