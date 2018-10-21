class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # beat 100% do it own
        def search(k):
            if k == 0 :return 0
            if search(k//2) == 1:
                return 1 - k %2
            else:
                return 0 + k %2
        return search(K-1)