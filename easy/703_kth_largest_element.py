import heapq
from typing import List


class KthLargest:
    """
    [8, 5, 4, 3, 2] # third place is 4
    [10, 8, 5, 5, 4, 3, 2] # third place is 5
    [10, 9, 8, 5, 5, 4, 3, 2] # third place is 8
    """
    def __init__(self, k: int, nums: List[int]):
        # Initialize parameters to be used in the class
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        # Pop-out smallest number(s) until heap size is k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        # Add val to heap
        heapq.heappush(self.min_heap, val)
        # Pop-out one value to keep heap size of k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # Smallest item in heap size k is the kth largest
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
kLargest = KthLargest(3, [4, 5, 8, 2])
print(kLargest.add(3))
print(kLargest.add(5))
print(kLargest.add(10))
print(kLargest.add(9))
print(kLargest.add(4))
