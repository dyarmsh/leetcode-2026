from typing import Optional
"""
[EASY] MERGE 2 SORTED LISTS
https://neetcode.io/problems/merge-two-sorted-linked-lists

Date: 14th Apr 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len of linked list
    - each node in list1 and list2 are looked at most once
Space: O(1)
    - re-ordered in-place
    - more intuitive approach IMO has space O(n)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ### Time: O(n), Space: O(1)
        # 1. find middle of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse second half to move in opp direction
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        """
        "I can solve this with O(1) space by finding the middle, reversing the second half, and then merging the two halves. 
        However, I want to note that while this optimizes for space complexity, it creates more complex code with three distinct operations that might be harder to maintain. 
        For a production environment, I might actually prefer the O(n) space solution using an array to store node references, as it's more readable and maintainable, unless memory constraints are a significant concern."
        -> This shows maturity and practical engineering judgment beyond just algorithmic knowledge. Many interviewers actually value this kind of nuanced thinking - it demonstrates that you're considering the broader engineering context, not just solving puzzles.
        """
        
        ### Time: O(n), Space: O(n)
        dummy = ListNode()
        node = head
        storage = []

        while node: # O(n)
            storage.append(node)
            node = node.next
                
        l = 0
        r = len(storage) - 1
        
        dummy.next = storage[l]

        while l < r:
            storage[l].next = storage[r]
            l += 1
            if l >= r:
                break
            storage[r].next = storage[l]
            r -= 1

        storage[l].next = None
