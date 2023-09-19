# Q1
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    #>>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"

    if n == 1:
        return m
    else:
        return multiply(m, n - 1) + m


print(multiply(5, 3))

# Q3
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...
    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * skip_mul(n - 2)

#4

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
    def check(m):
        if n == m:
            return True
        elif n % m == 0:
            return False
        else:
            return check(m+1)
    return check(2)


# 5

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements
    in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n %2 == 0:
        return hailstone(n//2)+1
    else:
        return hailstone(n*3+1)+1
# 错误点，没有return计数迭代次数

# 6
def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n1
    elif n2 == 0:
        return n2
    elif n1%10 > n2%10:
        return merge(n1,n2//10)*10+n2%10
    else:
        return merge(n1//10,n2)*10+n1%10
