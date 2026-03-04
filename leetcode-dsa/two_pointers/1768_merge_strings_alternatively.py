class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res_list = []

        n = min(len(word1), len(word2))

        for i in range(n):
            res_list.append(word1[i])
            res_list.append(word2[i])  

        res_list.append(word1[n:])
        res_list.append(word2[n:])

        return "".join(res_list)