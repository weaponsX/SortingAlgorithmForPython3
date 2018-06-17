# 交换排序-冒泡排序

"""
在要排序的一组数中，对当前还未排好序的范围内的全部数，自上而下对相邻的两个数依次进行比较和调整，让较大的数往下沉，较小的往上冒。
即：每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换。
"""

# 设置一标志性变量pos,用于记录每趟排序中最后一次进行交换的位置。
# 由于pos位置之后的记录均已交换到位,故在进行下一趟排序时只要扫描到pos位置即可。
def bubbleSort1(numbers):
    count = len(numbers)
    # 初始时,最后位置保持不变
    i = count - 1
    while i > 0:
        # 每趟开始时,无记录交换
        pos = 0
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                # 记录交换位置
                pos = j
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
        # 为下一趟排序做准备
        i = pos

# 传统冒泡排序中每一趟排序操作只能找到一个最大值或最小值,
# 我们考虑利用在每趟排序中进行正向和反向两遍冒泡的方法一次可以得到两个最终值(最大者和最小者)
# 从而使排序趟数几乎减少了一半。
def bubbleSort2(numbers):
    count = len(numbers)
    low = 0
    # 设置变量的初始值
    high = count - 1
    while low < high:
        # 正向冒泡，找到最大值
        for j in range(low, high):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        # 修改high值, 前移一位
        high = high - 1
        # 反向冒泡,找到最小值
        for j in range(high, low, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
        # 修改low值,后移一位
        low = low + 1

MyList = [3, 1, 5, 7, 2, 4, 9, 6]
# bubbleSort1(MyList)
bubbleSort2(MyList)

print(MyList)


