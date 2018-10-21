import collections
import heapq

# In Python, we improve this to O(N + k \log {N})O(N+klogN): our heapq.heapify operation and counting operations are O(N)O(N), and each of kk heapq.heappop operations are O(\log {N})O(logN).

# Space Complexity: O(N)O(N), the space used to store our count.
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        collect = collections.Counter(words)
        heap = [(-freq, word) for word, freq in collect.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
