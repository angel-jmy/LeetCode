class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low) % 2 or (low % 2 and high % 2):
            return (high - low) // 2 + 1
      
      
        return (high - low) // 2

        