"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""


def fit_to_width(string, limit):
    """Print string within a character limit."""

    # create output string
    # split the string along the spaces
    # count the chars in each new substring
    # if length of output string plus new string is under limit
    # add new string to output
    # else print output, clear it, add new string to it

    output = []
    words = string.split()

    for word in words:
        if len(" ".join(output) + " " + word) <= limit:
            output.append(word)
        else:
            print(" ".join(output))
            output = [word]

    print(" ".join(output))



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
