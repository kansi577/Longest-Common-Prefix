class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        s_1 = min(strs)
        s_2 = max(strs)
        
        for i, c in enumerate(s_1):
            if c != s_2[i]:
                return s_1[:i]
        return s_1
        
