#交换排序-快速排序

"""
快速排序是通常被认为在同数量级（O(nlog2n)）的排序方法中平均性能最好的。但若初始序列按关键码有序或基本有序时，快排序反而蜕化为冒泡排序。
为改进之，通常以“三者取中法”来选取基准记录，即将排序区间的两个端点与中点三个记录关键码居中的调整为支点记录。快速排序是一个不稳定的排序方法。
"""

def partition(numbers, low, high):
    i = low-1
    for j in range(low, high):
        if numbers[j] <= numbers[high]:
            i = i + 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i

# 递归实现
def quickSort(numbers, low, high):
    if low < high:
        # 将表一分为二
        privotLoc = partition(numbers, low, high)
        # 递归对低子表递归排序
        quickSort(numbers, low, privotLoc-1)
        # 递归对高子表递归排序
        quickSort(numbers, privotLoc+1, high)
    else:
        return

MyList = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
quickSort(MyList, 0, len(MyList)-1)
print(MyList)


