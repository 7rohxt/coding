"""
Sort Characters by Frequency

Given a string s, sort it in decreasing order based on the frequency
of the characters. Characters with higher frequency must come first.

If two characters have the same frequency, they can appear in any order.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation:
'e' appears twice, while 'r' and 't' appear once.
So 'e' must come before both 'r' and 't'.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc" or "cccaaa"

Example 3:
Input: s = "Aabb"
Output: "bbAa" or similar (case-sensitive)

Constraints:
- 1 <= len(s) <= 10^5
- s consists of English letters and digits.
"""

def frequency_sort(s):
    freq = {}

    for ch in s:
        if not ch in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    
    sorted_pairs = sorted(freq.items(), key=lambda x: x[1], reverse = True)

    # result = ""                               # every iteration creates a new string so time complexity O(n2)
    # for ch, count in sorted_pairs:
    #     result += ch*count

    result =[]
    for ch, count in sorted_pairs:
        result.append(ch*count)

    return ''.join(result)

print(frequency_sort("tree"))