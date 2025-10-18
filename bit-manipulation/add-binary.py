class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # lenA, lenB = len(a), len(b)
        res = ""
        adding = 0

        while a and b:
            va, vb = int(a[-1]), int(b[-1])
            _sum = va + vb + adding
            num = _sum % 2
            adding = _sum // 2
            res = str(num) + res
            a, b = a[:-1], b[:-1]

        _str = a if a else b if b else ''

        while _str:
            v = int(_str[-1])
            _sum = v + adding
            num = _sum % 2
            adding = _sum // 2
            res = str(num) + res
            _str = _str[:-1]

        if adding > 0:
            res = str(adding) + res

        return res


