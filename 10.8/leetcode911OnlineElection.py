import bisect


class TopVotedCandidate:
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leads, self.times, count = [], times, {}
        lead = -1
        # times or no times all AC
        for p in persons:
        # for t, p in zip(times, persons):

            count[p] = count.get(p, 0) + 1
            if (count[p] >= count.get(lead, 0)): lead = p
            self.leads.append(lead)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.leads[bisect.bisect(self.times, t) - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
