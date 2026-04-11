from typing import List

"""
[MEDIUM] DAILY TEMPERATURES
https://neetcode.io/problems/daily-temperatures/

Date: 10th Apr 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(temperatures)
Space: O(n)
    - where n = len(temperatures)
    - size of stack and result arrays
"""


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = [] # stores indices

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            top = stack.pop() # pop when new element breaks monotonically decreasing condition
            result[top] = i - top
        stack.append(i)
    
    return result