from math import factorial


def solve():
    n = 1896
    k = 983
    s = 0
    for i in range(k, n + 1):
        s += binomial(n, i) % 1000000
    print(int(s) % 1000000)

def mod(num, modulu):
    num = '{0:.10f}'.format(num)
    num = num.split('.')[0][-modulu:]
    return int(num)

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
