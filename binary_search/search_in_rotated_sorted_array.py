from typing import List

"""
[EASY] SEARCH IN ROTATED SORTED ARRAY
https://neetcode.io/problems/find-target-in-rotated-sorted-array

Date: 13th Apr 2026
Author: Diya Ramesh

Time: O(log(n))
    - where n = len(nums)
    - Worst case: O(log(n) + log(n) + log(n))
Space: O(1)
    - no additional memory used
"""

def search(nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1

    # finding pivot using binary search
    # pivot will separate into 2 sorted sub-arrays
    while lo < hi:
        mid = (hi - lo) // 2 + lo

        if nums[mid] > nums[hi]: # cut on the right
            lo = mid + 1
        else:
            hi = mid 
    
    pivot = lo

    def binary_search(nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1
    
    # using binary search on sorted sub-arrays
    left_res = binary_search(nums[:pivot], target)
    if left_res != -1:
        return left_res

    right_res = binary_search(nums[pivot:], target)
    if right_res != -1:
        right_res += pivot
    return right_res

print(search([3,4,5,6,1,2], 1))
print(search([3,5,6,0,1,2], 4))
print(search([4,5,6,7,0,1,2], 0))