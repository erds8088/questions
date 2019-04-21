"""
    两个单向链表有一个交点，找出这个交点
    思路：
        假如两个链表有交点，则从第一个相交的点开始，后面的点都是两个链表共用的。
        所以可以先获取两个链表长度差值n，然后较长链接指针后移n位。
        然后两个链表指针同时后移，判断是否相等。
"""

def find_node(linkedlistA, linkedlistB):
    len_A, len_B = 0, 0
    current_A, current_B = linkedlistA, linkedlistB
    while current_A:
        current_A = current_A.next
        len_A += 1
    while current_B:
        current_B = current_B.next
        len_B += 1

    current_A, current_B = linkedlistA, linkedlistB
    for i in range(abs(len_A-len_B)):
        if len_A > len_B:
            current_A = current_A.next
        else:
            current_B = current_B.next

    while current_A and current_B:
        if current_A == current_B:
            return current_A
        current_A, current_B = current_A.next, current_B.next
    return