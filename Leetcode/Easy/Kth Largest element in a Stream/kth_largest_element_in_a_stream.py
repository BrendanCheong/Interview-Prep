import heapq
class KthLargest:
    """
    The Binary Heap is like a self sorting list
    Each Operation is in O(log n)
    the idea is simple, we pop until the k == len(heap)
    so the time complexity is: 
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k;
        self.nums = nums[:]
        heapq.heapify(self.nums) #O(N) time, if we only heapify half the elements

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val) #O(log k)
        while len(self.nums) != self.k: # each operation is O(log k), we do this O(N-k) times
            heapq.heappop(self.nums) # remove all the small numbers, that means from a sorted list, remove until we get the kth largest element
        return self.nums[0] # take the top of the heap
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)