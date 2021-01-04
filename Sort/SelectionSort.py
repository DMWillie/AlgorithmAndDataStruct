"""选择排序"""

def selectionsort(arr):
    for i in range(len(arr)-1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minIndex]):
                minIndex = j

        # i不是最小数时，将i和最小数进行交换
        if i!=minIndex:
            arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr