"""
    原地快排
"""

def quicksort(lst, left, right):
    if left >= right:
        return
    slower=faster=left   # 定义两个快慢指针
    privot=lst[right]    # 中值为右端点的值，将比privot小的都移至privot左边
    while faster < right:
        if lst[faster] < privot:
            lst[faster], lst[slower] = lst[slower], lst[faster]
            slower+=1
        faster+=1
    # 循环结束后，slower停在了中值位置，此时应该把privot移至中值位置
    lst[faster], lst[slower] = lst[slower], privot
    # 对privot左右分别排序
    quicksort(lst, left, slower-1)
    quicksort(lst, slower+1, right)



s = [10, 2,3,1,5,8,9, 10, 13, 10, 10]
quicksort(s, 0, len(s)-1)

print(s)
