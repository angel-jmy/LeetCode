class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def single(int_):
            char = chr(ord('A') + int_ - 1)
            return char

        res = deque([])

        while columnNumber:
            mod = columnNumber % 26
            if mod == 0:
                mod = 26
                columnNumber = columnNumber // 26 - 1
            else:
                columnNumber //= 26
            d = single(mod)
            res.appendleft(d)

        return ''.join(list(res))
