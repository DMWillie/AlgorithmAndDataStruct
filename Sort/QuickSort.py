"""快速排序算法"""

def quickSort(arr,left=None,right=None):
    left = 0 if not isinstance(left,(int,float)) else left
    right = len(arr)-1 if not isinstance(right,(int,float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    # 基准元素
    pivot = left
    index = pivot+1
    i = index
    while i <= right:
        if arr[i]<arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [1,31,18,30,43,42,6,28,95,94]
    arr = quickSort(arr)
    print("调用快速排序后的数组为: ")
    print(arr)
