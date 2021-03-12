"""
输出九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (j, i, i*j), end='\t')
    print()
"""
如果没有第7行的print(),输出的结果会在一行中；
因为print()默认操作时换行（即end = '\n'），所以单独使用print()就是在每行结束时进行换行
"""