"""
19. Factorial Using Recursion

Write a function that takes a non-negative integer n and returns its factorial
using recursion.

The factorial of n (denoted as n!) is defined as:
n! = n × (n-1) × (n-2) × ... × 1
and 0! = 1.

Example 1:
Input: n = 5
Output: 120

Example 2:
Input: n = 0
Output: 1

Constraints:
- 0 <= n <= 20
"""
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))