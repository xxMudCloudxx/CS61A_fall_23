def remove(n,digit):
    """
    remove(231,3)
    21
    remove(243132,2)
    4313

    """
    kept,digits=0,0
    while n :
        n, last = n // 10, n % 10
        if digit != last:
            kept += 1
            digits += last*10**(kept-1)
    return digits
print(remove(8,2))