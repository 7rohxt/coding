"""
Fibonacci Using Recursion

Write a function that takes an integer n and returns the nth Fibonacci number
using recursion.

The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n >= 2

Example 1:
Input: n = 4
Output: 3

Example 2:
Input: n = 6
Output: 8

Constraints:
- 0 <= n <= 30

Note:
After implementing, be prepared to explain why the recursive approach
is inefficient and what its time complexity is.
"""

def fibonacci(n):
    if n<0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))