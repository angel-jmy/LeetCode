class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if not s:
            return s

        left = right = 0
        res = []
        curr = deque([])

        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            curr.append(c)

            if right == left:
                curr.pop()
                curr.popleft()
                left -= 1
                right -= 1
                res.extend(curr)
                curr = deque([])

        return ''.join(res)