from math import gcd

#Q1: Extending Rationals Q1：扩展有理数
#First, fill in the following code to implement the rational ADT from lecture.
def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> numer(a)
    1
    >>> denom(a)
    2
    """
    "*** YOUR CODE HERE ***"
    gcd_num = gcd(num, den)
    numer = num // gcd_num
    denom = den // gcd_num
    return [numer, denom]

def numer(rat):
    """Extracts the numerator from a rational number."""
    "*** YOUR CODE HERE ***"
    return rat[0]

def denom(rat):
    """Extracts the denominator from a rational number."""
    "*** YOUR CODE HERE ***"
    return rat[1]

# Divide
def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    "*** YOUR CODE HERE ***"
    num = numer(x) * denom(y)
    den = denom(x) * numer(y)
    return make_rat(num, den)

# Q3: Less Than
def lt_rat(x, y):
    """Returns True iff x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    "*** YOUR CODE HERE ***"
    return ( numer(x) * denom(y) - numer(y) * denom(x) ) < 0

# Tree
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree's list of branches is empty, and False otherwise."""
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root."""

    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


# Q5: Height
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    else:
        return 1+max([height(branch) for branch in branches(t)])

#Q7 :
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for branch in branches(t):
        path = find_path(branch, x)
        if path:
            return [label(t)] + path

def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t),[tree(leaf) for leaf in leaves])
    return tree(label(t),[sprout_leaves(branch,leaves) for branch in branches(t)])

# Q8
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    return sum([sum_tree(b) for b in branches(t)]) + label(t)

def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not balanced(b) :
            return False
    return True



