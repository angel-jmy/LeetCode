class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        days = [0] * N
        stack = []

        for i in range(N - 1, -1, -1):
            curr = temperatures[i]
            while stack and curr >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                days[i] = stack[-1] - i
            stack.append(i)

        return days