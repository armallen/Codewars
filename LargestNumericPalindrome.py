from itertools import combinations
from operator import mul


def build_palindromes(n):
    # Find frequency numbers, build a dict of pairs
    number_frequency = {}
    for c in set(n):
        number_frequency[c] = n.count(c)

    # Build palindrome iteratively, store only
    # left part and center number
    # pal = x1 x2 x3, ... xn , xn+1, xn, xn-1, ..., x1
    left_pal = []
    center = ''

    # Test all numbers
    # TODO : use only reverse sorted set of input numbers
    for i in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
        if i in number_frequency:
            # If odd frequency, use as center and extremity
            if number_frequency[i] % 2 == 1:
                if center == '':
                    center = i
                for j in range((number_frequency[i] - 1) / 2):
                    if i != '0':
                        left_pal.append(i)
                    else:
                        if len(left_pal) != 0:
                            left_pal.append(i)
            # If even frequency, only at extremity
            else:
                for j in range((number_frequency[i] / 2)):
                    if i != '0':
                        left_pal.append(i)
                    else:
                        if len(left_pal) != 0:
                            left_pal.append(i)

    # Build final palindrome
    pal = []
    for i in left_pal:
        pal.append(i)
    pal.append(center)
    for i in left_pal[::-1]:
        pal.append(i)
    return int("".join(pal))


# Compute the largest palindrome from
# all the possible input product combination
def numeric_palindrome(*args):
    biggest = 0
    # Test all product combinations without repetition
    for i in range(1, len(args)):
        for c in combinations(args, i + 1):
            curr = build_palindromes(str(reduce(mul, c, 1)))
            biggest = curr if curr > biggest else biggest
    return biggest
