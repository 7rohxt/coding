class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_map = {}
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1

        for ch in t:
            if ch not in s_map:
                return False

            s_map[ch] -= 1
            if s_map[ch] < 0:
                return False

        # return sum(s_map.values()) == 0
        return True 