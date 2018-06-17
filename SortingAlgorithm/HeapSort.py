# 选择排序-堆排序

"""
堆排序是一种树形选择排序，是对直接选择排序的有效改进。

而建堆时的比较次数不超过4n 次，因此堆排序最坏情况下，时间复杂度也为：O(nlogn )
"""

def sift(numbers, low, high):
    i = low
    j = 2*i+1
    temp = numbers[i]
    while j <= high:
        if j<high and numbers[j]<numbers[j+1]:
            j += 1
        if temp < numbers[j]:
            numbers[i] = numbers[j]
            i = j
            j = 2*i+1
        else:
            break
    numbers[i] = temp
    numbers[low], numbers[high] = numbers[low], numbers[high]

def heapSort(numbers):
    count = len(numbers)
    for i in range(count//2-1, -1, -1):
        sift(numbers, i, count-1)
    for i in range(count-1, -1, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        sift(numbers, 0, i-1)

MyList = [3, 1, 5, 7, 2, 4, 9, 6]
heapSort(MyList)
print(MyList)