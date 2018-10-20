import collections


class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if (len(people) <= 0):
            return 0
        pp = collections.deque(sorted(people))
        bnum = 0
        while (len(pp) > 1):
            if (pp[0] + pp[-1] <= limit):
                pp.pop()
                pp.popleft()
                bnum += 1
            else:
                pp.pop()
                bnum += 1
        if(len(pp) == 1):
            bnum += 1
        return bnum


if __name__ == '__main__':
    test = Solution()
    test.numRescueBoats(people=[2, 1], limit=3)
