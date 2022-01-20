import scipy.special
from math import factorial


def solve():
    n = 87
    k = 8
    print((scipy.special.binom(n, k) * factorial(k)) % 1000000)
