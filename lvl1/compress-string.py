"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""

    counter = 1
    output = string[0]
    last = output

    for rightIdx in range(1, len(string)):
        char = string[rightIdx]

        if char == last:
            counter += 1
        else:
            if counter > 1:
                output += str(counter)
            output += char    
            counter = 1
            last = char

    if counter > 1:
        output += str(counter)

    return output


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
