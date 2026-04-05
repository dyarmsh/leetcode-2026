"""
[EASY] VALID PARENTHESES
https://leetcode.com/problems/container-with-most-water/

Date: 17th March 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(s)
Space: O(n)
    - maximum size of stack (technically O(n/2) -> O(n))
"""

def isValid(s: str) -> bool:
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        # if closing bracket
        if char in matching_brackets:
            # as long as stack is NOT empty, check if top of stack has opening bracket
            if len(stack) != 0 and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
        # if opening bracket, add to stack
        else:
            stack.append(char)
    
    # if stack is empty -> valid
    return len(stack) == 0

