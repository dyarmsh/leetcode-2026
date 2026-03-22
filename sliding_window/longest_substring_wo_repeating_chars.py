"""
[MEDIUM] LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Date: 22nd March 2026
Author: Diya Ramesh

Time: O(n)
    - where n = len(s)
    - using sliding window approach :: each element is looked at most once
Space: O(m)
    - where m = number of unique characters in the string s
"""

def lengthOfLongestSubstring(s: str) -> int:

    chars = set()
    longest = 0
    l = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1

        chars.add(s[r])
        
        # technically, l -> r is not the longest substring
        # it just represents the length of it
        longest = max(longest, r-l+1)

    return longest
