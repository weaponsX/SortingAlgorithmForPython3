# 插入排序-希尔排序

"""希尔排序是1959 年由D.L.Shell 提出来的，相对直接排序有较大的改进。希尔排序又叫缩小增量排序。
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。"""

"""希尔排序时效分析很难，关键码的比较次数与记录移动次数依赖于增量因子序列d的选取，特定情况下可以准确估算出关键码的比较次数和记录的移动次数。
目前还没有人给出选取最好的增量因子序列的方法。
增量因子序列可以有各种取法，有取奇数的，也有取质数的，但需要注意：增量因子中除1 外没有公因子，且最后一个增量因子必须为1。
希尔排序方法是一个不稳定的排序方法。"""

def shellInsertSort(numbers):
    # 设定步长
    step = int(len(numbers)/2)
    while step>0:
        for i in range(step, len(numbers)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i>=step and numbers[i-step]>numbers[i]:
                numbers[i], numbers[i-step] = numbers[i-step], numbers[i]
                i -= step
        step = int(step/2)

MyList = [3, 1, 5, 7, 2, 4, 9, 6]
shellInsertSort(MyList)
print(MyList)






