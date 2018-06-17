# 插入排序-直接插入排序

"""插入排序是稳定的
时间复杂度：O（n^2）"""

def insertSort(numbers):
    n = len(numbers)
    for i in range(1, n):
        # 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
        if numbers[i] < numbers[i-1]:
            # 设置当前值前一个元素的标识
            j = i - 1
            x = numbers[i]
            numbers[i] = numbers[j]
            # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
            j = j-1
            while((x<numbers[j]) and j>=0):
                numbers[j+1] = numbers[j]
                j = j-1
            # 将临时变量赋值给合适位置
            numbers[j+1] = x

MyList = [3, 1, 5, 7, 2, 4, 9, 6]
insertSort(MyList)
print(MyList)






