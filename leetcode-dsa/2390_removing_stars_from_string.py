class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for ch in s:
            if ch == "*":
                if res: # added this to handle if first character is * or ehen res is emty and then star. - but not needed
                    res.pop()
                continue
            else:
                res.append(ch)
        
        return "".join(res)