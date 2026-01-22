from time import perf_counter_ns
from random import shuffle

def selection_sort(arr):
    pass

def quick_sort(arr):
    pass

def merge_sort(arr):
    pass

def insertion_sort(arr):
    pass

def counting_sort(arr):
    pass

def radix_sort(arr):
    pass

def heap_sort(arr):
    pass

def avl_sort(arr):
    pass

def main():
    size = int(input("Size of an array: "))
    print("1: Random\n2: Already sorted\n3: Reversed array")
    array_condition = input("Array Condition: ")
    algorithm = input("First letter of algorithm or all: ")
    
    array = list(range(size))
    
    if array_condition == "1":
        shuffle(array)
    elif array_condition == "3":
        array.reverse()
    elif array_condition not in ["1", "2", "3"]:
        print("Wrong input")
        exit(1)
    
    if algorithm == "all" or algorithm == "s":
        t0 = perf_counter_ns()
        selection_sort(array)
        t1 = perf_counter_ns()
        time_taken_s = t1-t0
    if algorithm == "all" or algorithm == "a":
        t0 = perf_counter_ns()
        avl_sort(array)
        t1 = perf_counter_ns()
        time_taken_a = t1-t0
    if algorithm == "all" or algorithm == "i":
        t0 = perf_counter_ns()
        insertion_sort(array)
        t1 = perf_counter_ns()
        time_taken_i = t1-t0
    if algorithm == "all" or algorithm == "h":
        t0 = perf_counter_ns()
        heap_sort(array)
        t1 = perf_counter_ns()
        time_taken_h = t1-t0
    if algorithm == "all" or algorithm == "q":
        t0 = perf_counter_ns()
        quick_sort(array)
        t1 = perf_counter_ns()
        time_taken_q = t1-t0
    if algorithm == "all" or algorithm == "m":
        t0 = perf_counter_ns()
        merge_sort(array)
        t1 = perf_counter_ns()
        time_taken_m = t1-t0
    if algorithm == "all" or algorithm == "c":
        t0 = perf_counter_ns()
        counting_sort(array)
        t1 = perf_counter_ns()
        time_taken_c = t1-t0
    if algorithm == "all" or algorithm == "r":
        t0 = perf_counter_ns()
        radix_sort(array)
        t1 = perf_counter_ns()
        time_taken_r = t1-t0
  

main()