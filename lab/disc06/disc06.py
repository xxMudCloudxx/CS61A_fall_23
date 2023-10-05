def filter_iter(iterable, f):
    """
    Generates elements of iterable for which f returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for x in iterable:
        if f(x):
            yield x

'''Q4: What's the Difference? Q4：有什么区别？

实现 differences ，一个生成器函数，它采用一个可迭代的 it ，其元素是数字。 differences 应该生成一个生成器，该生成器产生 it 的连续项之间的差异。
如果 it 的值少于 2 个，则 differences 应该不产生任何结果。'''
def differences(it):
    """
    Yields the differences between successive terms of iterable it.

    >>> d = differences(iter([5, 2, -100, 103]))
    >>> [next(d) for _ in range(3)]
    [-3, -102, 203]
    >>> list(differences([1]))
    []
    """
    "*** YOUR CODE HERE ***"
    it = iter(it)
    prev = next(it, None)
    for current in it:
        yield current - prev
        prev = current

'''
Q5: Primes Generator Q5：素数生成器
编写一个函数 primes_gen ，该函数接受单个参数 n ，并按降序生成小于或等于 n 的所有素数。假设 n >= 1 .您可以使用下面包含的 is_prime 函数，我们在讨论 3 中实现了该函数。
首先使用 for 循环并使用 yield 来解决此问题。
'''
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    "*** YOUR CODE HERE ***"
    ls = [i for i in range(2,n+1)][::-1]
    for num in ls:
        if is_prime(num):
            yield num

def primes_gen_2(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen_2(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)

def stair_ways(n):
    """
    Yields all ways to climb a set of N stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        yield []
    elif n == 1:
        yield [1]
    else:
        yield from ([1] + rest for rest in stair_ways(n - 1))
        yield from ([2] + rest for rest in stair_ways(n - 2))


