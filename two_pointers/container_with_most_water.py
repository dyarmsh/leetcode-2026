from typing import List

"""
[MEDIUM] CONTAINER WITH MOST WATER
https://leetcode.com/problems/container-with-most-water/

Date: 17th March 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(heights)
Space: O(1)
    - comparisons performed in-place
"""

def maxArea(heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, min(heights[l], heights[r]) * (r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
               
        return max_area

print(maxArea([1,7,1,1,1,1,2,5,12,3,500,50,7,8,4,7,38,9,10,12,6]))