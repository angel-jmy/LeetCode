class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        L = [arr[0]] + [0] * (N - 1)
        R = [0] * (N - 1) + [arr[-1]]

        for i in range(1, N):
            L[i] = max(L[i - 1] + arr[i], arr[i])
            R[N - i - 1] = max(R[N - i] + arr[N - i - 1], arr[N - i - 1])

        if N <= 2:
            return max(L)

        middle = max([L[i - 1] + R[i + 1] for i in range(1, N - 1)])
        middle = max(R[1], L[N - 2], middle)

        return max(middle, max(L))
