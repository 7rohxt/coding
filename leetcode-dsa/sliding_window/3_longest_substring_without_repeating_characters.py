class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left = 0
        seen = set()

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            cur_len = i - left + 1

            max_len = max(cur_len, max_len)
            seen.add(s[i])

        return max_len # if you want to return the sequence, store start = left when cur_sum > max_len everythime and return s[start:start + max_len] 