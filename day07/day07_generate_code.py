import random


def generate_code(code_len=4):
    """默认长度为4"""
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ' '
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    print(code)


generate_code(6)
