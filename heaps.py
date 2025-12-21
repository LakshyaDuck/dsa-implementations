import math
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def parent(self, i):
        return (i-1)//2
    def left(self, i):
        return 2*i + 1
    def right(self, i):
        return 2*i + 2
    def root(self):
        return self.heap[0]
    def height(self):
        return math.log2(self.size)
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = self.heap[i]  # BUG: should be `largest = i` (track index, not value)
        if self.size > l and self.heap[i] < self.heap[l]:  # BUG: should be `l < self.size` (check if index valid)
            largest = l
        if self.size > r and self.heap[largest] < self.heap[r]:  # BUG: should be `r < self.size` and `largest` is index, compare `self.heap[largest]`
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    def build_max_heap(self):
        for i in range(self.size, -1):  # BUG: should be `range(self.size // 2 - 1, -1, -1)` (start from last parent, go backwards)
            self.max_heapify(i)
    def sort(self):
        self.build_max_heap()
        n = self.size
        for i in range(n):
            self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
            self.size -= 1
            self.build_max_heap()  # BUG: inefficient - rebuilds entire heap. Should use heapify_down(0, self.size) instead