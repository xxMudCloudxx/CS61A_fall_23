# Q1: Count Stair Ways
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


# Q2: Count K
# Consider a special version of the count_stair_ways problem where we can take up to k steps at a time.
# Write a function count_k that calculates the number of ways to go up an n-step staircase. Assume n and k are positive integers.
def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"

    if n == 0:
        return 1
    elif n < 0:
        return 0
    total = 0
    for i in range(1, min(n, k) + 1):
        total += count_k(n - i, k)
    return total


# Q3
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


# Q4
from operator import mul


def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    global mul_result
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    ls = [s[::x] for x in range(2, len(s))]     # 封包切片后的子列表
    ls_count = []
    mul_result = 1
    for i in ls:
        for j in i:
            mul_result = mul(mul_result, j)     # 相乘子列表元素
            ls_count.append(mul_result)     # 存储每个子列表元素相乘后的结果
        mul_result = 1      # 重置计数器
    return max(ls_count)


def max_product_2(s):
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max([s[i] * s[j] for i in range(len(s)) for j in range(i, len(s)) if i != j])


# Q5
def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    "*** YOUR CODE HERE ***"
    def is_list(ls, store):
        for item in ls:
            if type(item) == list:
                is_list(item, store)
            else:
                store += [item]
    store=[]
    is_list(s,store)
    return store


