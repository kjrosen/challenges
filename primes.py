"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    >>> primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

"""

def is_prime(num):
    """checks if a number is prime"""

    from math import sqrt

    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    elif int(sqrt(num)) == sqrt(num):
        return False
        
    n = 3

    while n * n <= num:
        if num % n == 0:
            return False
        n += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes = []
    num = 2

    while count > 0:
        if is_prime(num):
            primes.append(num)
            count -= 1

        num += 1

    return primes



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
