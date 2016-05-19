from math import factorial
from operator import mul


def perms(element):
    list_elems = list(str(element))
    s = set(list_elems)
    frequencies = [list_elems.count(x) for x in s]
    return factorial(len(list_elems)) / reduce(mul, [factorial(x) for x in frequencies])
