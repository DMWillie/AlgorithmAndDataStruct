"""堆排序"""

def heapsort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr, 0, i)
        arrLen-=1
        heapify(arr, 0)
    return arr

def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i],arr[j] = arr[j],arr[i]


if __name__ == '__main__':
    arr = [1,31,18,30,43,42,6,28,95,94,53,99,43]
    arr = heapsort(arr)
    print("调用堆排序后的数组为: ")
    print(arr)