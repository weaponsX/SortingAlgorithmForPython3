# 归并排序

"""
归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。
然后再把有序子序列合并为整体有序序列。
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = int(len(numbers)/2)
    left = mergeSort(numbers[:mid])
    right = mergeSort(numbers[mid:])
    return merge(left, right)

MyList = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
MyList = mergeSort(MyList)
print(MyList)



