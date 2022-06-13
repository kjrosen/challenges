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


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    from math import sqrt

    primes = [2, 3, 5, 7, 11]

    if count == 0:
        return []
    elif count < 5:
        return primes[:count]
    elif count == 5:
        return primes

    else:
        to_check = primes[-1] + 1

        while len(primes) < count:
            is_prime = False

            square = sqrt(to_check)

            if int(square) == square:
                pass

            for prime in primes:
                if to_check % prime == 0:
                    is_prime = False
                    break
                
                is_prime = True
            
            if is_prime == True:
                primes.append(to_check)

            to_check += 1
            
    return primes



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
