def bninary_search_loop(arr, target):
    low = 0
    high = len(arr)
    mid = (low + high) / 2
    while high >= low:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
            mid = (low + high) / 2
        else:
            low = mid + 1
            mid = (low + high) / 2
    return None

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

def bninary_search_recursion(arr, target, low=None, high=None):
    if low == None or high == None:
        low = 0
        high = len(arr)
    if low > high:
        return None
    mid = (low + high) / 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bninary_search_recursion(arr, target, low=low, high=mid-1)
    else:
        return bninary_search_recursion(arr, target, low=mid+1, high=high)

def main():
    array = []
    size = int(input("Size of sorted array: "))
    for i in range(size):
        array.append(i)
    target = int(input(f"Number to found from 0 to {size - 1}: "))
    bsl = bninary_search_loop(array, target)
    ls = linear_search(array, target)
    bsr = bninary_search_recursion(array, target)

    print(f"{bsl} , {ls}, {bsr}")

main()
