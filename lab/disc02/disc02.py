''' Q5: Make Keeper '''
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True."""

    "*** YOUR CODE HERE ***"
    def cond(f):
        num = 1
        while num <= n:
            if f(num):
                print(num)
            num += 1
        return
    return cond
def is_even(x): # Even numbers have remainder 0 when divided by 2.
    return x % 2 == 0
make_keeper(5)(is_even)
    # 2
    # 4
make_keeper(5)(lambda x: True)
    # 1
    # 2
    # 3
    # 4
    # 5
make_keeper(5)(lambda x: False) # Nothing is printed

'''Q6: Currying'''
def curry(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = curry(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = curry(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> curry(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"



'''Q7: Make Your Own Lambdas'''
def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
# You can use more space on the back if you want


'''Q8: Match Maker
Implement match_k, which takes in an integer k and returns a function that takes in a variable x and returns True
if all the digits in x that are k apart are the same.
For example, match_k(2) returns a one argument function that takes in x and checks if digits that are 2 away in x
are the same.
match_k(2)(1010) has the value of x = 1010 and digits 1, 0, 1, 0 going from left to right. 1 == 1 and 0 == 0, so
the match_k(2)(1010) results in True.
match_k(2)(2010) has the value of x = 2010 and digits 2, 0, 1, 0 going from left to right. 2 != 1 and 0 == 0, so
the match_k(2)(2010) results in False.
Important: You may not use strings or indexing for this problem. You do not have to use all the lines; one staff
solution does not use the line directly above the while loop.
Hint: Floor dividing by powers of 10 gets rid of the rightmost digits.'''
def match_k(k):
    """Returns a function that checks if digits k apart match.
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
def ____________________________:
____________________________
while ____________________________:
if ____________________________:
return ____________________________
____________________________
____________________________
____________________________