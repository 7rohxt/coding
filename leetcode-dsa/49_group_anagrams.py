class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag_map = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word)) 

            if not sorted_word in anag_map:
                anag_map[sorted_word] = []
            
            anag_map[sorted_word].append(word)
        
        return anag_map.values()
