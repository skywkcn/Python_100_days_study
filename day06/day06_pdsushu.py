def is_prime(num):
    for x in range(2, int(num ** 0.5) + 1):
        s_prime = True
        if num % x == 0:
            s_prime = False
            break
    if s_prime:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)


is_prime(5)
