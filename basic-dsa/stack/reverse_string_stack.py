"""
Reverse a String Using a Stack

Given a string s, reverse the string using a stack data structure.

You must use a stack to perform the reversal.

Return the reversed string.

Example 1:
Input: s = "hello"
Output: "olleh"

Example 2:
Input: s = "Python"
Output: "nohtyP"

Example 3:
Input: s = ""
Output: ""

Constraints:
- 0 <= len(s) <= 10^4
- s consists of printable ASCII characters.
"""

def reverse_string(s):
    char_stack = []
    reversed_char = []

    for ch in s:
        char_stack.append(ch)
    
    for ch in range (len(char_stack)):
        reversed_char.append(char_stack.pop())   # Note: Previously used string += ch. but this creates new string everytime as they are immutable so O(n2)    
    return ''.join(reversed_char)

print(reverse_string("Python"))
        