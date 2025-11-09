class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                
            else:
                stack.append([c, 1])

            if c == ')' and stack[-1][1] == k:
                if stack[:-1] and stack[-2][0] == '(' and stack[-2][1] >= k:
                    stack.pop()
                    stack[-1][1] -= k
                    if stack[-1][1] == 0:
                        stack.pop()

        return ''.join(c * cnt for c, cnt in stack)