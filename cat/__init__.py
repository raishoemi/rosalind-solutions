import re
from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./cat/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq = f[0][1]
    print(get_noncrossing_perfect_matchings_count(seq, {})[0])

def get_noncrossing_perfect_matchings_count(seq: str, cache={}):
    if seq in cache:
        return cache[seq], cache
    if seq == '':
        return 1, cache
    if len(seq) % 2 != 0 or seq.count('G') != seq.count('C') or seq.count('A') != seq.count('U'):
        cache[seq] = 0
        return 0, cache
    if len(seq) == 2:
        cache[seq] = 1
        return 1, cache
    perfect_matchings_count = 0
    for i in range(1, len(seq), 2):
        if seq[0] == get_matching_bp(seq[i]):
            before = seq[1:i]
            after = seq[i+1:]
            before_perfect_matchings_count, new_cache = get_noncrossing_perfect_matchings_count(before, cache)
            cache = {**cache, **new_cache}
            if before == '' or before_perfect_matchings_count != 0:
                after_perfect_matchings_count, new_cache = get_noncrossing_perfect_matchings_count(after, cache)
                cache = {**cache, **new_cache}
                if after == '' or after_perfect_matchings_count != 0:
                    perfect_matchings_count += before_perfect_matchings_count * after_perfect_matchings_count
    cache[seq] = perfect_matchings_count
    return perfect_matchings_count, cache

def get_matching_bp(bp: str) -> str:
    if bp == 'A':
        return 'U'
    elif bp == 'U':
        return 'A'
    elif bp == 'C':
        return 'G'
    return 'C'
