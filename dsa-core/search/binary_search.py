"""
Binary Search

Given a sorted array of integers nums in ascending order and an integer target,
write a function to search for target in nums.

If target exists in the array, return its index.
Otherwise, return -1.

You must implement an algorithm with O(log n) time complexity.

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i], target <= 10^4
- nums is sorted in ascending order.
"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid        
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


print(binary_search([-1,0,3,5,9,12], 9))
print(binary_search([-1,0,3,5,9,12], 2))