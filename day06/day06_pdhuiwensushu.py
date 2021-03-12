def is_prime(num):
    x = num
    reversed_num = 0
    p_prime = False
    s_prime = True
    # 判断是否为回文数
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    if reversed_num == x:
        p_prime = True

    # 判断是否为素数
    for i in range(2, int(num ** 0.5) + 1):
        s_prime = True
        if num % i == 0:
            s_prime = False
            break
    if p_prime and s_prime:
        print('%d是回文素数' % x)
    else:
        print('%d不是回文素数' % x)


is_prime(5)
