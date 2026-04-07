from collections import defaultdict
"""
[MEDIUM] Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Date: 3rd April 2026
Author: Diya Ramesh

Time: O(n) (Worst case)
    - where n = len(s)
    - looking at n windows at most
Space: O(m) (Worst case)
    - where n = # unique chars in s
    - size of the hash map
"""   

def characterReplacement(s: str, k: int) -> int:
    l = 0
    count = defaultdict(int)
    res = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] += 1
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, (r - l + 1))

    return res