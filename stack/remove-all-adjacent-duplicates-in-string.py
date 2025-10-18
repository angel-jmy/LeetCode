class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        stack = deque()

        stack.append(s[0])

        for i in range(1, N):
            if not stack:
                stack.append(s[i])
                continue

            last = stack.pop()
            if s[i] == last:
                continue
            else:
                stack.append(last)
                stack.append(s[i])

        return ''.join(stack)
        