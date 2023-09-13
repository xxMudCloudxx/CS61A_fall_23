def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.


    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1

    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]

    return dice


from random import randint


def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'

    def dice():
        return randint(1, sides)

    return dice


four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    dice_result = []
    total = 0
    while num_rolls > 0:
        dice_result.append(dice())
        if 1 in dice_result:
            total = 1
            num_rolls -= 1
        else:
            total = sum(dice_result)
            num_rolls -= 1
    return total
    # END PROBLEM 1
def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's3.83
    3.0
    """

    # BEGIN PROBLEM 8
    def return_function(*args):
        for i in args:
            total_count = original_function(samples_count, i)
            print(float(total_count // samples_count))

    return return_function
    # END PROBLEM 8
dice = make_test_dice(4, 2, 5, 1)
averaged_dice = make_averaged(roll_dice, 40)
averaged_dice(1, dice)