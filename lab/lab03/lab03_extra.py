""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    return is_prime_helper(n, n - 1)

def is_prime_helper(n, i):
    if i == 1:
        return True
    elif n % i == 0:
        return False
    else:
        return is_prime_helper(n, i - 1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    return ten_pairs_helper(n, [0,0,0,0,0,0,0,0,0,0])

def ten_pairs_helper(n, count):
    if n == 0:
        return 0
    else:
        digit = n % 10
        tmp = 0
        if digit != 0:
            tmp = count[10 - digit]
        
        count[digit] += 1

        return ten_pairs_helper(n // 10, count) + tmp