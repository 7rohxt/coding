class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        
        for i in range(left, n):
            nums[i] = 0
        
        return nums
        