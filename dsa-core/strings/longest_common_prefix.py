"""
Problem: Longest Common Prefix

Given a list of strings `strs`, return the longest common prefix string 
among all the strings.

If there is no common prefix, return an empty string "".

A prefix is a substring that appears at the beginning of a string.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"
Explanation: All strings start with "fl".

Constraints:
- 0 ≤ len(strs) ≤ 200
- 0 ≤ len(strs[i]) ≤ 200
- strs[i] consists of lowercase English letters.
"""


def longest_common_prefix(strs):

    first = strs[0]

    for i in range(len(first)):
        for s in strs[1:]:
            if i >= len(s) or first[i] != s[i]:
                return first[:i]
                
        
    return first
    
print(longest_common_prefix(["flower","flow","flight"]))