class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        N = len(plants)
        l, r = 0, N - 1
        remainA = capacityA
        remainB = capacityB
        refills = 0
        while l < r:
            if plants[l] <= remainA:
                remainA -= plants[l]
            else:
                remainA = capacityA
                remainA -= plants[l]
                refills += 1

            if plants[r] <= remainB:
                remainB -= plants[r]
            else:
                remainB = capacityB
                remainB -= plants[r]
                refills += 1

            l += 1
            r -= 1

        if l == r:
            if remainA >= remainB:
                if plants[l] <= remainA:
                    remainA -= plants[l]
                else:
                    remainA = capacityA
                    remainA -= plants[l]
                    refills += 1

            elif remainA < remainB:
                if plants[r] <= remainB:
                    remainB -= plants[r]
                else:
                    remainB = capacityB
                    remainB -= plants[r]
                    refills += 1

        return refills