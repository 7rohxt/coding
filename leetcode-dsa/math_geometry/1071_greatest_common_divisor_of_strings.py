class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        len1, len2 = len(str1), len(str2)

        def is_divisor(l):
            if len1 % l != 0 or len2 % l != 0:
                return False
            
            str1_fraction = len1 // l
            str2_fraction = len2 // l

            base_candidate = str1[:l] # or str2[:l] --> doesnt matter
            if str1_fraction * base_candidate == str1 and str2_fraction * base_candidate == str2:
                return True

            
        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                return str1[:l]
        
        return ""

