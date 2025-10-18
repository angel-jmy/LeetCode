class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        mapping = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        res = []

        def backtrack(index, path):
            # If we've processed all digits, add the path to results
            if index == len(digits):
                res.append("".join(path))
                return

            # Go through each letter for this digit
            for ch in mapping[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()  # backtrack


        backtrack(0, [])
        return res

