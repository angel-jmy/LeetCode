class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def single(char):
            idx = ord(char) - ord('A') + 1
            return idx

        res = 0
        for c in columnTitle:
            num = single(c)
            res = 26 * res + num

        return res