class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        
        freq = Counter(nums)  # --- Counter is faster

        nums.sort(key = lambda x:(freq[x], -x))  # --- (a,b) is sort by 'a' first. if tie, then sort by 'b'.
        return nums