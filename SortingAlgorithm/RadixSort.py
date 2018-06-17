# 桶排序/基数排序

"""
桶排序非常浪费空间, 比如需要排序的范围在0~2000之间, 需要排序的数是[3,9,4,2000], 同样需要2001个空间
注意: 通排序不能排序小数
"""

def radixSort(numbers):
    # 选一个最大的值
    max_num = max(numbers)
    # 创建一个元素全是0的列表，当做桶
    bucket = [0] * (max_num + 1)
    # 把所有元素放入桶中，既把对应元素个数加一
    for i in numbers:
        bucket[i] += 1
    # 存储排序好的元素
    sort_numbers = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_numbers.append(j)
    return sort_numbers

MyList = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
MyList = radixSort(MyList)
print(MyList)





