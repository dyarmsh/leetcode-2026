from collections import defaultdict
from typing import List

"""
[MEDIUM] GROUP ANAGRAMS
https://leetcode.com/problems/group-anagrams/

Date: 8th March 2026
Author: Diya Ramesh

Time: O(m*n) (Worst case)
    - where m = len(strs) (# words in strs list)
    - where n = average length of word in strs
Space: O(m*n) (Worst case)
    - where m = len(strs) (# words in strs list) :: max size of anagrams dict
    - where n = average length of word in strs
    - anagrams dict stores {(0,0,...,0): [str1, str2, ...], ...}
        - where str1, str2, ... strm have an average length of n characters
"""   

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # dict that handles missing keys and creates [] as values
    anagrams = defaultdict(list) # at most O(m)

    for word in strs: # O(m)
        char_freq = [0] * 26
        for char in word: # O(n)
            char_freq[ord(char) - ord("a")] += 1

        anagrams[tuple(char_freq)].append(word) # using tuple as key as it is immutable

        # defaultdict eliminates these steps
        # if anagrams.get(tuple(char_freq)) is None:
        #     anagrams[tuple(char_freq)] = [word]
        # else:
        #     anagrams[tuple(char_freq)].append(word)
        
    return list(anagrams.values())




"""
Second solution 
Time: O(m * nlog(n))
    - where m = len(strs) :: words in str
    - where n = avg word length :: total chars in strs
        - O(nlog(n)) because of sorting
Space: O(m * n)
    - where m = len(strs) :: words in str
    - where n = avg word length :: total chars in strs
"""
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    # anagrams = {}
    # for index, word in enumerate(strs): # O(m)
    #     sorted_word = "".join(sorted(word)) # O(nlog(n))
    #     if anagrams.get(sorted_word) is None or index == 0:
    #         anagrams[sorted_word] = [word]
    #     else:
    #         anagrams[sorted_word].append(word)

    # return list(anagrams.values())


"""
First solution - inefficient, but correct
Time: O(m^2 * m)
    - where m = len(strs) :: words in str
    - where n = avg word length :: total chars in strs
Space: O(m * n)
    - where m = len(strs) :: words in str
    - where n = avg word length :: total chars in strs
        - however O(n) = O(26) = O(1), since there can be at most 26 characters as keys in word_dict
"""
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
#     word_dicts = []
#     anagrams_lst = []
#     for index, word in enumerate(strs): # O(n)
#         word_dict = {}

#         for char in word: # O(m)
#             word_dict[char] = word_dict.get(char, 0) + 1
        
#         if index == 0:
#             anagrams_lst.append([strs[index]])
#             word_dicts.append(word_dict)
#         else:
#             if word_dict in word_dicts: # O(n)
#                 if word_dicts.index(word_dict) >= len(anagrams_lst):
#                     anagrams_lst.insert(word_dicts.index(word_dict),[word])
#                 else:
#                     anagrams_lst[word_dicts.index(word_dict)].append(word)
                    
#             else:
#                 word_dicts.append(word_dict)
#                 anagrams_lst.insert(word_dicts.index(word_dict),[word])
    
#     return anagrams_lst