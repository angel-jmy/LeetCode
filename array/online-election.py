class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        N = len(persons)
        self.prefs = [0] * N # id of the max_count candidate so far
        self.prefs[0] = persons[0]
        # max_person = 0
        max_count = 0
        counts = defaultdict(int)
        for i in range(N):
            counts[persons[i]] += 1
            if counts[persons[i]] >= max_count:
                max_count = counts[persons[i]]
                self.prefs[i] = persons[i]
            elif i > 0:
                self.prefs[i] = self.prefs[i - 1]

        # self.persons = persons
        self.times = times

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1
        
        return self.prefs[idx]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)