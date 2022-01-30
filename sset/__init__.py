from math import factorial, pow
import scipy.special


def solve():
    n = 898

    # Doesn't work, maybe because of python and large numbers handling, kinda stupid
    p = 1  # empty set and full set
    results = []
    for i in range(1, n + 1):
        results.append(mod(binomial(n, i), 6))
        p += mod(binomial(n, i), 6)
        p = p % 1000000
    print(p % 1000000)
    print((sum(map(lambda x: x % 1000000, results)) % 1000000) + 1)

    # For some reason does work, need to check why
    print(pow(2, n) % 1000000)

def mod(num, modulu):
    num = '{0:.10f}'.format(num)
    num = num.split('.')[0][-modulu:]
    return int(num)

def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
