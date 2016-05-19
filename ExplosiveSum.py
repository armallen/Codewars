# Dictionary of already computed partitions
partitions = {}


# Define key
def hash(a, b):
    return "".join([str(a), " ", str(b)])


# Recursive partition function
def partition(sum, largest_number):
    # We cannot go further, no number left
    if largest_number == 0:
        return 0
    # We managed to find a solution : +1
    if 0 == sum:
        return 1
        # The number substracted is too big : not a solution
    if 0 > sum:
        return 0

    # If it is already computed, no recursive call
    if hash(sum, largest_number) in partitions:
        return partitions[hash(sum, largest_number)]

    # Recursive call
    partitions[hash(sum, largest_number)] = partition(sum, largest_number - 1) + partition(sum - largest_number,
                                                                                           largest_number)
    return partitions[hash(sum, largest_number)]


# Computation function
def exp_sum(n):
    if n < 0:
        return 0
    if n != 0:
        return 1 + partition(n, n - 1)
    return 1
