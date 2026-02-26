class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_map = {}

        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in seen_map:
                return list((seen_map[complement], i))

            seen_map[nums[i]] = i       