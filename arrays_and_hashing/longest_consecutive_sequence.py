"""
[MEDIUM] LONGEST CONSECUTIVE SEQUENCE
https://leetcode.com/problems/longest-consecutive-sequence/

Date: 15th March 2026
Author: Diya Ramesh

Time: O(n) (worst case)
    - where n = len(nums)
    - technically O(2n) worst case :: each element is accessed at most twice
Space: O(n) (worst case)
    - where n = len(nums)
    - size of hash set: nums
"""

from typing import List

def longestConsecutive(nums: List[int]) -> int:

    nums = set(nums)
    max_length = 0

    for num in nums: 

        # finding first element in sequence
        if num-1 not in nums: # O(1)
            seq_length = 1
            while num+seq_length in nums:
                seq_length+=1

            max_length = max(max_length, seq_length)
    
    return max_length