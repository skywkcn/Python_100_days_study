def pn(num):
    """判断一个数是不是回文数"""
    x = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)
    if x == reversed_num:
        print('%d是回文数' % reversed_num)
    else:
        print('%d不是回文数' % reversed_num)
    return


pn(123432)
