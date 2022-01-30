def solve():
    n = 89342
    x = 0.415558
    s = 'CGTGCTTC'
    at_count = s.count('A') + s.count('T')
    at = (1 - x) / 2
    gc_count = s.count('G') + s.count('C')
    gc = x / 2
    print(1 - (1 - (at**at_count * gc**gc_count))**n)
