class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            left = i + 1
            right = n - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                total = nums [i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left+=1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif total > 0:
                    right -= 1
                
                else:
                    left += 1
        
        return res