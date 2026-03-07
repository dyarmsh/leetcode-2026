"""
[EASY] VALID ANAGRAM
https://leetcode.com/problems/valid-anagram/

Date: 7th March 2026
Author: Diya Ramesh

Time: O(N) (worse case)
    - where N = len(s) or len(t) :: when they are equal
Space: O(N) (worst case)
    - where N = len(s) or len(t) :: when they are equal
    - size of dictionary
"""

def isAnagram(s: str, t: str) -> bool:

    if len(s) == len(t):

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return (s_dict == t_dict)

    return False



        