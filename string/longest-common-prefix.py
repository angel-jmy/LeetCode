class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs)
        
        len0 = len(strs[0])
        lenN = len(strs[-1])

        i = 0
        longest = ""

        while i < len0 and i < lenN:
            if strs[0][i] == strs[-1][i]:
                longest = longest + strs[0][i]
                i += 1
                
            else:
                break

        return longest
                



        


        