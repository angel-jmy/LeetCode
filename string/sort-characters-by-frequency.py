class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)

        ans = []

        for char, freq in sorted(counts.items(), key = lambda x: -x[1]):
            ans.append(char * freq)

        return ''.join(ans)