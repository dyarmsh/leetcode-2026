from typing import List

"""
[MEDIUM] PRODUCT OF ARRAY EXCEPT SELF
https://leetcode.com/problems/product-of-array-except-self/

Date: 16th March 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(nums)
    - building prefix, suffix and output arrays all take O(n) each
Space: O(n)
    - where n = len(nums)
"""

def productExceptSelf(nums: List[int]) -> List[int]:
    
    pref = [0] * len(nums)
    suff = [0] * len(nums)
    result = [0] * len(nums)

    pref[0] = 1
    suff[len(nums)-1] = 1

    # constructing prefix array, 
    # where pref[i] = prod(all elems up to i (excl))
    for i in range(1, len(nums)):
        pref[i] = nums[i-1] * pref[i-1]
    
    # constructing suffix array, 
    # where suff[i] = prod(all elems up to i (excl))
    for i in range(len(nums)-2, -1, -1):
        suff[i] = nums[i+1] * suff[i+1]

    for i in range(len(nums)):
        result[i] = pref[i] * suff[i]

    return result