"""
Merge Sort

Given an unsorted array of integers nums, implement the Merge Sort
algorithm to sort the array in ascending order.

You must not use any built-in sorting functions.

Merge Sort works using the divide-and-conquer approach:

1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the two sorted halves into one sorted array.

Return the sorted array.

Example 1:
Input: nums = [5, 3, 8, 4, 2, 7, 1, 6]
Output: [1, 2, 3, 4, 5, 6, 7, 8]

Example 2:
Input: nums = [10, -1, 2, 5, 0]
Output: [-1, 0, 2, 5, 10]

Example 3:
Input: nums = [1]
Output: [1]

Constraints:
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

"""
def merge_sort (nums):
    if len(nums) <= 1:
        return nums
    

    mid = (len(nums)) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1


    return sorted_list

print(merge_sort([5, 3, 8, 4, 2, 7, 1, 6]))