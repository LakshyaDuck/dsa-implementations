from heaps import Heap

def find_min(arr, i):
    min = i
    for j in range(i, len(arr)):
        if arr[min] > arr[j]:
            min = j
    return min

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def identify_position(arr, i):
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i]:
            return j + 1
        
def insert_at_from(arr, i, j):
    temp = arr[j]
    for k in range(i, j):
        arr[i + 1] = arr[i]
    arr[i] = temp

def create_heap(arr):
    return Heap(arr)

def heap_sort(arr):
    return create_heap(arr).sort()