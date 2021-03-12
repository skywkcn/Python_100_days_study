"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:   # 此步没看懂
                result += num // factor
    if result == num:
        print(num)

"""
以下代码是自己写的，与上述代码运行相比，少了一个1
for num in range(2, 10000):
    y = 1  # 此式如果放入下面的for循环，会出错
    for x in range(2, num):
        d = num % x
        if d == 0:  # 此步和上式可以合并
            y = y + x
    if num == y:
        print(num)
"""
