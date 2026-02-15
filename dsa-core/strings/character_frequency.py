"""
Problem: Character Frequency in a String

Given a string `s`, return a dictionary containing the frequency 
(count) of each character in the string.

The function should count every character, including letters, digits, 
spaces, and special characters, exactly as they appear.

Example:
Input:  "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Example:
Input:  "aab! "
Output: {'a': 2, 'b': 1, '!': 1, ' ': 1}

Constraints:
- 0 ≤ len(s) ≤ 10^5
- The string may contain any printable ASCII characters.

Notes:
- The solution should run in O(n) time.
- Avoid using external libraries unless explicitly allowed.
"""

def char_freq(s):
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq

print(char_freq("aab!"))

# Better solution would be

def char_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_freq("aab!"))
