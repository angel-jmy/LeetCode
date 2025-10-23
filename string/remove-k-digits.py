class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # if k remains, remove from the end (largest suffix)
        while k:
            stack.pop()
            k -= 1

        # strip leading zeros; return "0" if empty
        res = ''.join(stack).lstrip('0')
        return res or "0"