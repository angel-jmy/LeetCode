class ExamTracker:

    def __init__(self):
        self.times = []
        self.pref = [0]
        self.length = 0

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.pref.append(self.pref[-1] + score)
        self.length += 1

    def totalScore(self, startTime: int, endTime: int) -> int:
        def lowerbound(times, starttime):
            N = self.length
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if times[mid] < starttime:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def upperbound(times, endtime):
            N = self.length
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if times[mid] > endtime:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        l = lowerbound(self.times, startTime)
        r = upperbound(self.times, endTime)

        # print(l)
        # print(r)
        # print(self.times)
        # print(self.pref)

        return self.pref[r + 1] - self.pref[l]

        
        


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)