class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        N = len(persons)
        self.prefs = [0] * N
        if persons[0] == 1:
            self.prefs[0] = 1
        else:
            self.prefs[0] = -1
        for i in range(1, N):
            num = 1 if persons[i] == 1 else -1
            self.prefs[i] = self.prefs[i - 1] + num

        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1
        if self.prefs[idx] > 0:
            return 1
        if self.prefs[idx] < 0:
            return 0
        
        return self.persons[idx]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)