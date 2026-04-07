"""
[MEDIUM] MIN STACK
https://leetcode.com/problems/min-stack

Date: 7th Apr 2026
Author: Diya Ramesh
"""
class MinStack:

    def __init__(self):
        """
        Space: O(2*n) = O(n)
        """

        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Time: O(1)
        """

        self.stack.append(val)
        
        if not self.min_stack: # if min_stack is EMPTY -> push val
            self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]: # if val is min -> push val
                self.min_stack.append(val)
            elif val >= self.min_stack[-1]: # dupe added to handle pop()
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        """
        Time: O(1)
        """

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        Time: O(1)
        """

        return self.stack[-1]

    def getMin(self) -> int:
        """
        Time: O(1)
        """
        
        return self.min_stack[-1]
        
