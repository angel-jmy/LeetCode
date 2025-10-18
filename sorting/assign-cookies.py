class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        g_i, s_i = 0, 0
        g_N, s_N = len(g), len(s)

        while g_i < g_N and s_i < s_N:
            if g[g_i] <= s[s_i]:
                g_i += 1
            s_i += 1
        
        return g_i