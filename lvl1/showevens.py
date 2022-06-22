"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""

def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    evens = []
    for idx, num in enumerate(nums):
        if num % 2 == 0:
            evens.append(idx)

    return evens


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
