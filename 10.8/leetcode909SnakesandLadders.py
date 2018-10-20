class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = int(len(board[0]))
        step = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) // n, (i - 1) % n
                num = board[~a][b if a % 2 == 0 else ~b]
                if num > 0:
                    i = num
                if i == n * n:
                    return step[x] + 1
                if i not in step:
                    step[i] = step[x] + 1
                    bfs.append(i)
        return -1
