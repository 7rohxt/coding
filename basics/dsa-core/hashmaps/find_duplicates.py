"""
Find All Duplicates in a List

Given an integer array nums of length n, return a list of all elements
that appear more than once in the array.

Each duplicate element should appear only once in the result.
You may return the answer in any order.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
- 1 <= n <= 10^5
- 1 <= nums[i] <= n

Follow-up:
Can you solve it in O(n) time and without using extra space
(other than the output list)?
"""
def find_duplicates(nums):
    duplicates = set()
    num_map = {}
    for i in range(len(nums)):
        if not nums[i] in num_map:
            num_map[nums[i]] = 1
        else:
            duplicates.add(nums[i])

    return duplicates 

print(find_duplicates([4,3,2,7,8,2,3,3,3,1]))
