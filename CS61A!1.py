from math import pi
radius=20
area=20*20*pi   #1256.6370614359173

#我们可以发现当radius改变时，area并不会更新
#此时我们需要构建函数更新area:
def area():
    return pi*radius*radius
radius=10
print(area())

#-------------------------------
'''
python -m doctest -v xx.py
'''
'''
xx.py:

    >>> defunction(10)
    3
'''
#--------------------------------
from operator import  floordiv,mod,truediv,Modulo
def op(n,d):
    return floordiv(n,d),mod(n,d),truediv(n,d)
a,b,c=op(2012,10)
print(a,b,c)
print(floordiv(2013,1000))

