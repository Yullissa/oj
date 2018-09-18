import heapq
import sys


def printmid(mid1, mid2):
    if (mid1 + mid2) % 2 == 0:
        print (mid1 + mid2) / 2
    else:
        print(float(mid1 + mid2) / 2)


n = int(sys.stdin.readline())
maxHeap = []
minHeap = []
heapq.heapify(maxHeap)
heapq.heapify(minHeap)
mid = -1

for i in range(n):
    p, q = sys.stdin.readline().strip().split(" ")
    q = int(q)
    if p == 'A':
        if mid == -1:
            mid = q
        elif q >= mid:
            heapq.heappush(minHeap, q)
        else:
            heapq.heappush(maxHeap, -q)
    elif p == 'R':
        if q < mid:
            if -q in maxHeap:
                maxHeap.remove(-q)
        elif q > mid:
            if q in minHeap:
                minHeap.remove(q)
        elif q == mid:
            if len(maxHeap) > len(minHeap):
                mid = -heapq.heappop(maxHeap)
            elif len(maxHeap) < len(minHeap):
                mid = heapq.heappop(minHeap)
            elif len(maxHeap) == len(minHeap):
                if len(maxHeap) == 0:
                    mid = -1
                else:
                    mid = heapq.heappop(minHeap)
    while len(maxHeap) - len(minHeap) >= 2:
        heapq.heappush(minHeap, mid)
        mid = -heapq.heappop(maxHeap)
    while len(minHeap) - len(maxHeap) >= 2:
        heapq.heappush(maxHeap, -mid)
        mid = heapq.heappop(minHeap)
    if len(maxHeap) > len(minHeap):
        printmid(-maxHeap[0], mid)
    elif len(maxHeap) < len(minHeap):
        printmid(minHeap[0], mid)
    else:
        if mid == -1:
            print 0
        else:
            print mid
