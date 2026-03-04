class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        res = []
        for i in range(len(s)):
            if s[i] in valid_map.values():
                res.append(s[i])
            
            else:
                if not res or not res.pop() == valid_map[s[i]]:
                    return False
                    
        return len(res) == 0 
                