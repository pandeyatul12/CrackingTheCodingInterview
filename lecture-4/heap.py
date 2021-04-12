from heapq import *

minheap = []

for num in [2, 3, 11, 12, 15, 13, 65, 34, 22, 1, 6]:
    heappush(minheap, num)

print(minheap[0])
