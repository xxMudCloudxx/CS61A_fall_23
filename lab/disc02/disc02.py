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


def match_k(k):
    def apart(n):
        if k == 1 and n ==1:
            return True
        part_1, part_2 = n % (10 ** k), n // (10 ** k)
        return part_1 == part_2
    return apart
print(match_k(2)(1010))
print(match_k(2)(2010))
print(match_k(1)(1010))
print(match_k(1)(1))
print(match_k(1)(2111111111111111))

def f4():
    # f4()()(3)()
    # 3
    return lambda :lambda x:lambda :x
print(f4()()(3)())


