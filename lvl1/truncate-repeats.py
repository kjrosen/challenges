"""Truncate repeating characters into one character.

For example:

>>> truncate('aaaaabbbbbcccaaaa')
'abca'

>>> truncate('hi there')
'hi there'

The function should be able to handle special characters, punctuation, and/or
numbers:

>>> truncate('hi   !!! wooow')
'hi ! wow'
"""

def truncate(string):
    """Truncate repeating characters in a string."""

    out = string[0]

    for char in string:
        if char == out[-1]:
            pass
        else:
            out += char
    
    return out


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
