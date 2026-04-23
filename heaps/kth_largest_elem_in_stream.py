from heapq import heapify, heappop, heappush
from typing import List

"""
[EASY] KTH LARGEST ELEMENT IN STREAM
https://neetcode.io/problems/kth-largest-integer-in-a-stream

Date: 23rd Apr 2026
Author: Diya Ramesh

Time for add(): O(m * log(k))
    - where m = # times add() is called
    - k is the largest number to be tracked
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Time: O(n), as n >= k
            - where n = len(nums) originally
            - for heapify()

        Space: O(n), as n >= k
        """

        self.k = k
        self.min_heap = nums
        heapify(nums) # O(n)
        
        while len(self.min_heap) > self.k:
            heappop(self.min_heap) # O(log(n))

    def add(self, val: int) -> int:
        """
        Time: O(m * log(k))
            - where m = # times add() is called
            - heappush and heappop are O(log(k))
        Space: O(1)
            - not consuming / creating extra space
        """

        heappush(self.min_heap, val) # O(log(k))

        if len(self.min_heap) > self.k:
            heappop(self.min_heap) # O(log(k))
        
        return self.min_heap[0]