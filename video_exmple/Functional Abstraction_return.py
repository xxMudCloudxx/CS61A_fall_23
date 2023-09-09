def search(f):
    x = 0
    while not f(x):
        x += 1
    return x
    # while True:
    #     if f(x):
    #         return x
    #     x += 1

def is_three(x):
    return x == 3

def square(x):
    return x*x

def positive(x):
    return max(0,square(x)-100)

def inverse(f):
    return lambda y:search(lambda x: f(x) == y)

sqrt = inverse(square())
'''
inverse 函数接受一个函数 f 作为参数，然后返回一个新的函数，这个新函数将接受一个参数 y。
当调用这个新函数并传入 y 时，它会在整数序列中搜索 x 的值，使得 f(x) == y 成立，然后返回找到的 x 值。
它允许您通过已知输出值来查找输入值。
'''