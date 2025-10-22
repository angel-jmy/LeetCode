class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op.isdigit() or re.match(r'\-\d+', op):
                res.append(int(op))
            elif op == '+':
                res.append(res[-1] + res[-2])
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == 'C':
                res.pop()

        return sum(res)