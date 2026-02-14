"""
Group Strings by Anagrams

Given an array of strings strs, group the anagrams together.
You may return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= len(strs) <= 10^4
- 0 <= len(strs[i]) <= 100
- strs[i] consists of lowercase English letters.
"""

def anagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word)) # why "".join()? coz sorted(word) -> ['a','e','t']

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())



print(anagrams(["eat","tea","tan","ate","nat","bat"]))