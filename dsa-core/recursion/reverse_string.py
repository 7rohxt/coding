"""
Reverse a String Using Recursion

Write a function that takes a string s and returns the reversed string
using recursion.

You must not use built-in reverse functions.

Example 1:
Input: s = "hello"
Output: "olleh"

Example 2:
Input: s = "Python"
Output: "nohtyP"

Constraints:
- 0 <= len(s) <= 10^4
"""

def reverse_string(s):
    
    if len(s) == 0:
        return s

    return reverse_string(s[1:])+s[0]

print(reverse_string("python"))
