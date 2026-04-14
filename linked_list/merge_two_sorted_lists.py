from typing import Optional
"""
[EASY] MERGE 2 SORTED LISTS
https://neetcode.io/problems/merge-two-sorted-linked-lists

Date: 14th Apr 2026
Author: Diya Ramesh

Time: O(m + n)
    - where m = len(list1), n = len(list2)
    - each node in list1 and list2 are looked at most once
Space: O(1)
    - merged in-place using dummy node
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode() # anchor
    node = dummy # acts as pointer

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2 # appends rest of whatever list still has elements

    return dummy.next