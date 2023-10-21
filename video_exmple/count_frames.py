def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max:
            counted.max = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max = 0
    return counted