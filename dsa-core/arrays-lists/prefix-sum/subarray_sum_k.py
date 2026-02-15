"""
Subarray With Sum K

Given an integer array nums and an integer k,
check whether there exists a contiguous subarray
whose sum equals k.

Return True if such a subarray exists,
otherwise return False.

Example 1:
Input: nums = [1, 2, 3], k = 5
Output: True
Explanation: The subarray [2, 3] has sum 5.

Example 2:
Input: nums = [1, 2, 3], k = 7
Output: False

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# Brute Force Solution
# def subarray_sum_k(nums, k):

#     for i in range(len(nums)):
#         cur_sum = 0

#         for j in range (i, len(nums)):
#             cur_sum += nums[j]

#             if cur_sum == k:

#                 return True

#     return False

# print(subarray_sum_k([1, 2, 3], 6))

def subarray_sum_k(nums, k):
    prefix_sums = set()
    cur_sum = 0

    for i in range(len(nums)):
        
        cur_sum += nums[i]
        
        if cur_sum == k:
            return True

        if cur_sum - k in prefix_sums:
                return True
        prefix_sums.add(cur_sum)

    return False
             
print(subarray_sum_k([1, 2, 3], 6))