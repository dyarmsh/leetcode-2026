from typing import List

"""
[EASY] BINARY SEARCH
https://neetcode.io/problems/binary-search

Date: 11th Apr 2026
Author: Diya Ramesh

Time: O(log(n))
    - where n = len(nums)
Space: O(1)
    - no additional memory used
"""


def search(nums: List[int], target: int) -> int:

    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = ((hi - lo) // 2) + lo # + lo to avoid overflow

        if target < nums[mid]:
            hi = mid - 1

        elif target > nums[mid]:
            lo = mid + 1
    
        else:
            return mid
    
    return -1