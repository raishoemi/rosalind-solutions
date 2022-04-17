def solve():
    n = 817473
    dna = 'GCTATCACTG'
    gc_array = map(
        float, '0.000 0.100 0.116 0.158 0.226 0.272 0.314 0.367 0.441 0.452 0.523 0.556 0.605 0.664 0.726 0.795 0.819 0.876 0.915 1.000'.split(' '))
    results = []
    for gc in gc_array:
        result = n - 1
        for nucleotide in dna:
            if nucleotide == 'G' or nucleotide == 'C':
                result *= gc / 2
            else:
                result *= (1 - gc) / 2
        results.append(result)
    print(' '.join(map(lambda x: str(x)[:6], results)))
