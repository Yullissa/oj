class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        dfs = [0]
        seen = set(dfs)

        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
        if len(seen) == len(rooms):
            return True
        else:
            return False
