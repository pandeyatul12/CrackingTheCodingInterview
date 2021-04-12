from heapq import *

def topK(nums, k):
    minHeap = []

    # insert first k in heap
    for i in range(k):
        heappush(minheap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)

def kthSmallest(nums, k):
    maxHeap = []

    # insert first k in heap
    for i in range(k):
        heappush(maxHeap, -nums[i])

    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    return -maxHeap[0]
