from typing import Optional

"""
[EASY] REVERSE LINKED LIST
https://neetcode.io/problems/reverse-a-linked-list

Date: 13th Apr 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len of linked list
Space: O(1)
    - reversed in-place by moving pointers
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        # 1. store next node
        temp = curr.next
        # 2. point curr to prev
        curr.next = prev
        # 3. prev becomes curr
        prev = curr
        # 3. curr becomes next node
        curr = temp
    return prev # return prev bc curr will be None 