from collections import defaultdict
from typing import List

"""
[MEDIUM] TOP K FREQUENT ELEMENTS
https://leetcode.com/problems/top-k-frequent-elements/

Date: 9th March 2026
Author: Diya Ramesh

Time: O(n) (Worst case)
    - where n = len(nums)
    - using Bucket sort variation instead of sorting brings from O(nlog(n)) -> O(n)
Space: O(n) (Worst case)
    - where n = len(nums)
    - frequencies dict and counts is at most n elements
        - res is at most k elements, and k <= n
"""   

def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequencies = defaultdict(int)

    for num in nums:  # O(n)
        frequencies[num] += 1

    counts = [[] for _ in range(len(nums))]

    for num, freq in frequencies.items(): # O(n)
        counts[freq - 1].append(num)
    
    res = []
    i = len(counts)
    while len(res) < k and i >= 0:
        if len(counts[i-1]) > 0:
            for elem in counts[i-1]: # O(n)
                res.append(elem)
        i -= 1

    return(res)

    # ALTERNATE SOLUTION: 
    # # O(nlogn) - sorting frequencies in dictionary
    # freq_lst = (sorted(frequencies.items(), key=lambda freq: freq[1], reverse = True))
    # return [x[0] for x in freq_lst[:k]] # O(n)


