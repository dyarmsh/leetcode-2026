"""
[MEDIUM] 3Sum
https://leetcode.com/problems/3sum/

Date: 14th March 2026
Author: Diya Ramesh

Time: O(n^2)
    - where n = len(nums)
Space: O(n)
    - where n = len(nums)
"""
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    
    nums.sort() # O(nlog(n))

    valid_triplets = []

    for f in range(len(nums)): # O(n)
        if nums[f] > 0:
            break

        if f != 0 and nums[f] == nums[f-1]:
            continue
        else:
            l = f + 1
            r = len(nums)-1

            while l < r: # worse case: O(n) 
                if nums[f] + nums[l] + nums[r] == 0:
                    valid_triplets.append([nums[l], nums[f], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[f] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[f] + nums[l] + nums[r] > 0:
                    r -= 1

    return valid_triplets