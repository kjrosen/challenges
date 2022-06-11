"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe.
    
    find difference between each hole and each cafe
    """

    max_distance = 0

    for hole in range(num_holes):
        ## begin by assuming closest cafe is fully across the chain
        closest = num_holes

        for cafe in cafes:
            distance = abs(hole-cafe)
            closest = min(distance, closest)

        max_distance = max(closest, max_distance)

    return max_distance


def furthest_optimized(num_holes, cafes):
    """use a binary search and bisect to 
    """

    from bisect import bisect_left

    max_travel = 0

    for hole in range(num_holes):

        ##bisect_left returns the index where hole would go
        # if hole were added to the sorted list that is cafes
        idx = bisect_left(cafes, hole)

        ## if index is after all cafes, closest is the last cafe
        if idx == len(num_holes):
            pass
    
        ## if index is before all cafes, closest is the first cafe
        elif idx == 0:
            pass

        ## if the index IS the hole, no travel necessary
        elif cafes[idx] == hole:
            pass

        ## else the hole is between two cafes
        # find difference to get distance to both, then take the shorter as closest
        else:
            pass






        

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
