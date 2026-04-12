from typing import List

"""
[MEDIUM] FIND MINIMUM IN ROTATED SORTED ARRAY
https://neetcode.io/problems/find-minimum-in-rotated-sorted-array

Date: 12th Apr 2026
Author: Diya Ramesh

Time: O(log(n))
    - where n = len(nums)
Space: O(1)
    - no additional memory used
"""

def findMin(nums: List[int]) -> int:

    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (hi - lo) // 2 + lo

        if nums[mid] > nums[hi]: # look  right
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]