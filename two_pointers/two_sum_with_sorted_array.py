"""
[MEDIUM] TWO SUM II (WITH SORTED ARRAY)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Date: 13th March 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(numbers)
Space: O(1)
    - only comparisons performed and always [int, int] returned
"""

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:

    # two pointers
    i = 0
    j = len(numbers) - 1

    while i < j:

        # we can do this since the array is sorted
        if numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            return [i+1, j+1]
                

        
            
