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

    ### More optimal by jumping l straight to correct pos ###
    # imo, this is more intuitive
    chars_map = {}
    l = 0
    longest = 0

    for r in range(len(s)):
        if chars_map.get(s[r]) is not None:
            print(s[r])
            l = max(chars_map[s[r]] + 1, l)
        
        chars_map[s[r]] = r
        longest = max(longest, r-l+1)
    return longest
    ###
    
    chars_map = {}
    l = 0
    longest = 0

    for r in range(len(s)):
        if chars_map.get(s[r]) is not None:
            print(s[r])
            l = chars_map[s[r]] + 1
            chars_map[s[r]] = r
        
        chars_map[s[r]] = r
        longest = max(longest, r-l+1)
    return longest

print(lengthOfLongestSubstring("abcabcbb"))