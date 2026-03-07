from typing import List

"""
[EASY] CONTAINS DUPLICATE
https://leetcode.com/problems/contains-duplicate/

Date: 7th March 2026
Author: Diya Ramesh

Time: O(N) (Worst case)
    - where N = len(nums)
    - looping through nums
Space: O(N) (Worst case)
    - where N = len(nums)
    - max size of nums_set
"""    

def containsDuplicate(nums: List[int]) -> bool:

    nums_set = set()

    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)

    return False


# this approach is not as efficient
# not necessary to store #occurences so use set instead

# nums_dict = {}

# for num in nums:    # O(N)
#     if nums_dict.get(num, 0) > 1: # O(1)
#         return True
    
#     nums_dict[num] = nums_dict.get(num, 1) + 1 # O(1)

# return False