from itertools import permutations


def solve():
    symbols = 'E C S F M Z Q H W V P'.split()
    n = 3
    with open('./lexv/solution', 'w') as f:
        for p in lexv(symbols, n):
            f.write(f'{p}\n')
    
def lexv(symbols, n):
    if n == 1:
        return symbols
    p = []
    for s in symbols:
        p.append(s)
        for sub_s in lexv(symbols, n - 1):
            p.append(f'{s}{sub_s}')
    return p
