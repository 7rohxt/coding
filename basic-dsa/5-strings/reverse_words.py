"""
Problem: Reverse Words in a String

Given a string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The input string may contain leading spaces, trailing spaces, 
or multiple spaces between words.

Return a new string where:
- The words appear in reverse order.
- Words are separated by a single space.
- There are no leading or trailing spaces.

Example:
Input:  "  hello world  "
Output: "world hello"

Example:
Input:  "a good   example"
Output: "example good a"

Constraints:
- 1 ≤ len(s) ≤ 10^4
- The string may contain letters, digits, and spaces.
"""
# using built-ins
def reverse_words(s):
    words = s.split()
    return " ".join(reversed(words))


# using two pointer
def reverse_words(s):
    words = s.split()

    left = 0
    right = len(words)-1
    while left < right:
        words[left], words[right] = words[right], words[left]

        left += 1
        right -=1
    
    return " ".join(words)

# print(reverse_words("Hello world"))


# without split

def reverse_words(s):
    words = []
    word = ""

    for char in s:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
        
    if word:
        words.append(word)

    result = " ".join(words[::-1])
    return result


print(reverse_words("Hello world"))