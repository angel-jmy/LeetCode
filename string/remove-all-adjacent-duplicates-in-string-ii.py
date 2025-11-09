class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # each item: [char, run_length]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()       # delete this run of k
            else:
                stack.append([ch, 1])

        # rebuild string
        return "".join(ch * cnt for ch, cnt in stack)
