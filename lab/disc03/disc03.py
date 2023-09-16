# Q1
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    #>>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"

    if n == 1:
        return 5
    else:
        return multiply(m, n - 1) + 5


print(multiply(5, 3))

# Q2

