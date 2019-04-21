"""
问题:
    如何用Python实现一个N进制转化

    其余的26或64进制类似，只需要给出对应的mapping
"""

def generic_radix(n, mapping, number):
    s = ""
    while number >= n:
        current = number % n
        s = mapping[current] + s
        number = (number - current) // n
    return mapping[number]+s


def to_sixteen(number):
    m = {
        0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
        10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F",
    }
    return generic_radix(16, m, number)


def to_eight(number):
    m = {
        0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7"
    }
    return generic_radix(8, m, number)



print(to_sixteen(0))
print(to_eight(19))
    