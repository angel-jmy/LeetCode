class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        N = len(cards)
        min_size = N + 1
        last_seen = {}

        for r in range(N):
            if cards[r] not in last_seen:
                last_seen[cards[r]] = r
            
            else:
                new_size = r - last_seen[cards[r]] + 1
                if new_size < min_size:
                    min_size = new_size
                last_seen[cards[r]] = r

        return min_size if min_size < N + 1 else -1