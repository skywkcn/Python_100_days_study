"""
判断一个正整数是否为素数
"""
from math import sqrt

num = int(input('请输入一个正整数： '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

"""
以下代码为求100以内的素数
from math import sqrt
for x in range(2, 100):
    is_prime = True
    for y in range(2, int(sqrt(x)) + 1):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        print(x)

"""