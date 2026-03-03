class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left = 0
        s_len = len(s)

        for right in range(len(t)):
            if left < s_len:                    # if left >= length of substring -> out of index error (check with s= "")
                if t[right] == s[left]:
                    left += 1
        
        return left == s_len