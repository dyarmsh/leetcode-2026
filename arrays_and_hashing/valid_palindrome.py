"""
[EASY] VALID PALINDROME
https://leetcode.com/problems/valid-anagram/

Date: 7th March 2026
Author: Diya Ramesh

Time: O(N) (worst case)
    - where N = len(s)
Space: O(1) (worst case)
    - no space being taken
"""

def isPalindrome(s: str) -> bool:

    # two pointers
    l = 0
    r = len(s) - 1

    while l < r:

        # ensuring characters are alphanumeric
        if s[l].isalnum() == True and s[r].isalnum() == True: 
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        # shifting pointer when characters are NOT alphanumeric
        if s[l].isalnum() == False:
            l += 1
        if s[r].isalnum() == False:
            r -= 1

    return True  