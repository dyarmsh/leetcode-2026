"""
[MEDIUM] 3SUM
https://leetcode.com/problems/3sum/

Date: 12th March 2026
Author: Diya Ramesh

Time:
Space: 
"""

def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    print(nums)

    fixed = 0
    left = 1
    right = len(nums) - 1

    lst = []
    for i in range(len(nums)):
        while left < right:
            # print("here1!", [nums[fixed], nums[left], nums[right]])
            if nums[fixed] + nums[left] + nums[right] == 0 and [nums[fixed], nums[left], nums[right]] not in lst:
                # print("here2!", [nums[fixed], nums[left], nums[right]])
                lst.append([nums[fixed], nums[left], nums[right]])
            
            left += 1
            #right -= 1
        fixed += 1
        left = fixed + 1
        right = len(nums) - 1
