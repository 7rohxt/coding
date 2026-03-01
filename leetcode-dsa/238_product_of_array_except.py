class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        prefix_prods = [1] * n
        for i in range (1, n):
            prefix_prods[i] = prefix_prods[i - 1] * nums[i - 1]

        suffix_prods = [1] * n
        for i in range (n-2, -1, -1):
            suffix_prods[i] = suffix_prods[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix_prods[i] * suffix_prods[i]

    
        return res

        
        