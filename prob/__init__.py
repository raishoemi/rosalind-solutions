from math import log


def solve():
    seq = 'CAATGCCAGCGCTTTTCAGGAAATCTCAGCTATGCTGAGGCCGCTTCGTACAGCCCTTGTTTGCACTGGAATGTCTAGACGCAACGGACTACGT'
    probabilities = map(float, '0.071 0.142 0.184 0.232 0.260 0.342 0.374 0.415 0.452 0.508 0.572 0.617 0.671 0.730 0.783 0.843 0.873 0.933'.split(' '))
    gc_count = seq.count('G') + seq.count('C')
    at_count = len(seq) - gc_count
    result = []
    for pgc in probabilities:
        pat = (1 - pgc) / 2
        pgc = pgc / 2
        result.append(log(pgc**gc_count * pat**at_count, 10))
    print(' '.join(map(lambda f: str(f)[:9], result)))
