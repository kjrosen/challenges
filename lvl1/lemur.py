"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    ## if the next branch is dead, jump 2
    ## if the next branch is alive, check branch after that
        ## if that branch is alive jump 2
        ## else jump 1

    jumps = 0
    skip = 0

    if len(branches) == 1:
        return 0
    elif len(branches) <= 3:
        return 1


    for idx in range(len(branches)-2):
        if skip > 0:
            skip -= 1

        else:
            jumps += 1

            if branches[idx + 2] == 0:
                skip = 1

    return jumps


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")