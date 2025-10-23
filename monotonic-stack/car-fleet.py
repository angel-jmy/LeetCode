class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        times = list(map(lambda pos, sp: (target - pos) / sp, position, speed))
        combined = list(zip(position, times))
        combined.sort(key = lambda x: x[0])

        stack = []
        for i in range(N - 1, -1, -1):
            if stack and combined[i][1] <= combined[stack[-1]][1]:
                pass           
            else:
                stack.append(i)

        return len(stack)