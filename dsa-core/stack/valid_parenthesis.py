"""
Valid Parentheses

Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every closing bracket has a corresponding open bracket of the same type.

Return True if the string is valid, otherwise return False.

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "([)]"
Output: False

Example 5:
Input: s = "({[]})"
Output: True

Constraints:
- 1 <= len(s) <= 10^4
- s consists only of parentheses characters: '()[]{}'.
"""

def valid_parenthesis(s):
    stack=[]
    pairs = {
        ')':'(', 
        ']':'[',
        '}':'{'
         }

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
            # print(f"{ch} added")

        else:
            if not stack:
                return False
            
            popped = stack.pop()
            if popped != pairs[ch]:
                return False
        
        # print(stack)
        
    return len(stack) == 0

print(valid_parenthesis("({[]})"))

