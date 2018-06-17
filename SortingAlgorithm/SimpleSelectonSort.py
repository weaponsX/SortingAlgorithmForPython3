# 选择排序-简单选择排序

"""
在要排序的一组数中，选出最小（或者最大）的一个数与第1个位置的数交换；
然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换，依次类推，直到第n-1个元素（倒数第二个数）和第n个元素（最后一个数）比较为止。

简单选择排序的改进——二元选择排序
简单选择排序，每趟循环只能确定一个元素排序后的定位。
我们可以考虑改进为每趟循环确定两个元素（当前趟最大和最小记录）的位置,从而减少排序所需的循环次数。改进后对n个数据进行排序，最多只需进行[n/2]趟循环即可
"""

# 简单选择排序
def selectSort(numbers):
    for i in range(len(numbers)-1):
        min = i
        for j in range(i+1, len(numbers)):
            if numbers[min] > numbers[j]:
                min = j
        if min != i:
            numbers[i], numbers[min] = numbers[min], numbers[i]

# 二元选择排序
def selectSort2(numbers):
    count = len(numbers)
    for i in range(1, int(count/2)):
        # 做不超过n/2趟选择排序
        # 分别记录最大和最小关键字记录位置
        min = i
        max = i
        for j in range(i+1, count-i):
            if numbers[j] > numbers[max]:
                max = j
                continue
            elif numbers[j] < numbers[min]:
                min = j
        # 该交换操作还可分情况讨论以提高效率
        tmp = numbers[i-1]
        numbers[i-1] = numbers[min]
        numbers[min] = tmp
        tmp = numbers[count-i]
        numbers[count-i] = numbers[max]
        numbers[max] = tmp


MyList = [3, 1, 5, 7, 2, 4, 9, 6]
# selectSort(MyList)
selectSort2(MyList)
print(MyList)

