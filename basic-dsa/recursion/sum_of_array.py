"""
Sum of Array Using Recursion

Write a function that takes a list of integers nums and returns the sum
of all elements using recursion.

Example 1:
Input: nums = [1,2,3,4]
Output: 10

Example 2:
Input: nums = []
Output: 0

Constraints:
- 0 <= len(nums) <= 10^4
- -10^4 <= nums[i] <= 10^4
"""

def sum_of_array(nums):
    
    if len(nums) == 0: # or simple -- if not nums:
        return 0
        
    return nums[0] + sum_of_array(nums[1:]) # when nums = [1], nums[1:] -. empty not index error (slicing)

print(sum_of_array([1]))