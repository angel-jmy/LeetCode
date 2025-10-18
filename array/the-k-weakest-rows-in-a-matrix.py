class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Convert the 2d matrix to a dictionary
        strengths = {idx: sum(elem) for idx, elem in zip(range(len(mat)), mat)}

        # Sort the dictionary
        keys = sorted(strengths.keys(), key = lambda i: strengths[i])

        return keys[:k]

        ##### ANOTHER WAY #####
        # m = len(mat)
        # rows = sorted(range(m), key=lambda i: (mat[i], i))

        # del rows[k:]

        # return rows


