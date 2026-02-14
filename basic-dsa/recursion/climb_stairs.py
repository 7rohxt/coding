"""
Climbing Stairs Problem

An animal is trying to reach the top of a staircase with n steps.
It can climb either 1 step or 2 steps at a time.

Write a function that returns the total number of distinct ways
to reach the nth step.

Example 1:
Input: n = 2
Output: 2
Explanation:
1 + 1
2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1
1 + 2
2 + 1

Constraints:
- 1 <= n <= 45

"""

def climb_stairs (n):
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(2))
print(climb_stairs(3))