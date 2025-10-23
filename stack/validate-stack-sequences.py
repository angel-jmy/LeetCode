class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = j = 0
        N = len(pushed)

        while i < N and j < N:
            if pushed[i] != popped[j]:
                if stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
            elif pushed[i] == popped[j]:
                stack.append(pushed[i])
                stack.pop()
                i += 1
                j += 1

        while j < N:
            if stack and popped[j] != stack[-1]:
                return False
            if not stack:
                return False

            stack.pop()
            j += 1


        return True