import time
def trace(func):
    def 包装(*args, **kwargs):
        缩进 = "  " * 包装.递归深度
        调用字符串 = f"{func.__name__}({', '.join(map(repr, args))})"
        print(f"{缩进}开始 {调用字符串} - {time.strftime('%H:%M:%S')}")
        包装.递归深度 += 1
        结果 = func(*args, **kwargs)
        包装.递归深度 -= 1
        print(f"{缩进}结束 {调用字符串} 返回 {结果} - {time.strftime('%H:%M:%S')}")
        return 结果

    包装.递归深度 = 0
    return 包装
