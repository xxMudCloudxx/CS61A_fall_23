'''
Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
Write a function that takes in the current temperature and a boolean value telling if it is raining. This function
should return True if Alfonso will wear a jacket and False otherwise.
'''
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    # if raining:
    #     return True
    # elif temp < 60:
    #     return True
    # else:
    #     return False
    return temp < 60 or raining

'''
Write a function that takes in a positive number n and rounds n to the nearest ten.
Solve this problem using an if statement
'''
def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    if n % 10 <= 4:
        return n-n%10
    else:
        return ((n//10)+1)*10
    #return (n+5)//10*10
'''
Implement the classic Fizz Buzz sequence. The fizzbuzz function takes a positive integer n and prints out a single
line for each integer from 1 to n. For each i:
• If i is divisible by both 3 and 5, print fizzbuzz.
• If i is divisible by 3 (but not 5), print fizz.
• If i is divisible by 5 (but not 3), print buzz.
• Otherwise, print the number i
'''
def fizzbuzz(n):
    """
>>> result = fizzbuzz(16)
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
>>> print(result)
None
    """
    num = 0
    while num < n:
        num += 1
        if num % 3 ==0 and num % 5 ==0:
            print('fizzbuzz')
        elif num % 3 ==0:#and num % 5 !=0:
            print('fizz')
        elif num % 5 ==0: #and num % 3 !=0:
            print('buzz')
        else:
            print(num)

'''
Write a function that returns True if a positive integer n is a prime number and False otherwise.
A prime number n is a number that is not divisible by any numbers other than 1 and n itself. For example, 13 is
prime, since it is only divisible by 1 and 13, but 14 is not, since it is divisible by 1, 2, 7, and 14.
'''
def is_prime(n):
    """
>>> is_prime(10)
False
>>> is_prime(7)
True
>>> is_prime(1) # one is not a prime number!!
False
    """
    if n != 1:
        if n % 2 == 0:
            return False
        else:
            return True
    else:
        return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n.
>>> unique_digits(8675309) # All are unique
7
>>> unique_digits(13173131) # 1, 3, and 7
3
>>> unique_digits(101) # 0 and 1
2
    """
    "*** YOUR CODE HERE ***"
    uni=0
    while n > 0:
        num,n = n % 10,n//10
        if not has_digit(n,num):
            uni += 1
    return uni
def has_digit(n, k):
    """Returns whether k is a digit in n.
>>> has_digit(10, 1)
True
>>> has_digit(12, 7)
False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n >0:
       if n % 10 == k:
           return True
       else:
           n=n//10
           has_digit(n,k)
    return False
