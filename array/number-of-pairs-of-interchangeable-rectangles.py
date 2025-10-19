class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = {}
        pairs = 0
        for w, h in rectangles:
            ratio = w / h
            if ratio in counts:
                pairs += counts[ratio]

            counts[ratio] = counts.get(ratio, 0) + 1

        return pairs

        # counts = defaultdict(int)
        # for w, h in rectangles:
        #     ratio = w / h
        #     counts[ratio] += 1

        # pairs = 0
        # for n in counts.values():
        #     pairs += n * (n - 1) // 2

        # return pairs