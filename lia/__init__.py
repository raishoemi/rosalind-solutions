import scipy.special
from tqdm import tqdm

def solve():
    p_hetero = 0.25
    p_not_hetero = 1 - p_hetero
    n = 19
    k = 6
    proginey_amount = 2 ** k
    p = 0
    for _ in tqdm(range(n, proginey_amount + 1)):
        p += scipy.special.binom(proginey_amount, _) * (p_hetero ** _) * (p_not_hetero ** (proginey_amount - _))
    print(p)
