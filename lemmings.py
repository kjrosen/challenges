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

    >>> furthest_optimiziest(7, [0, 6])
    3

    >>> furthest_optimiziest(3, [0, 1, 2])
    0

    >>> furthest_optimiziest(3, [2])
    2

    >>> furthest_optimiziest(3, [0])
    2

    >>> furthest_optimiziest(6, [2, 4])
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
        if idx == len(cafes):
            dist = hole - cafes[-1]
    
        ## if index is before all cafes, closest is the first cafe
        elif idx == 0:
            dist = cafes[0] - hole

        ## if the index IS the hole, no travel necessary
        elif cafes[idx] == hole:
            dist = 0

        ## else the hole is between two cafes
        # find difference to get distance to both, then take the shorter as closest
        else:
            dist = min(hole - cafes[idx-1], cafes[idx] - hole)

        max_travel = max(dist, max_travel)

    return max_travel


def furthest_optimiziest(num_holes, cafes):
    """find the distance between the cafes rather than the holes"""

    distances = [cafes[0], (num_holes - 1) - cafes[-1]]

    ##find the distance between each cafe
    # split in half
    for idx in range(1, len(cafes)):
        distances.append(
            (cafes[idx] - cafes[idx-1]) // 2
        )

    return max(distances)


        

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
