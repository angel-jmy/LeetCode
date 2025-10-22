class Solution:
    def removeStars(self, s: str) -> str:
        lst = []

        for c in s:
            if c != '*':
                lst.append(c)
            else:
                lst.pop()

        return ''.join(lst)
