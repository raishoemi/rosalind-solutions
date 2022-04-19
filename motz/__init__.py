import re
from typing import Tuple
from Bio.SeqIO.FastaIO import SimpleFastaParser
from tqdm import tqdm


def solve():
    input_file = open('./motz/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq = f[0][1]
    print(motzkin(seq, {}, True))

def motzkin(seq: str, cache: dict, first_run=False) -> int:
    if len(seq) <= 1:
        return 1
    if seq in cache:
        return cache[seq]
    matchings = 0
    iterator = tqdm(range(1, len(seq))) if first_run else range(1, len(seq))
    for i in iterator:
        if seq[i] == get_matching_bp(seq[0]):
            before_seq = seq[1:i]
            after_seq = seq[i+1:]
            before_result = motzkin(before_seq, cache)
            cache[before_seq] = before_result
            after_result = motzkin(after_seq, cache)
            cache[after_seq] = after_result
            matchings += ((before_result * after_result) % 1000000)
    next_motzkin = motzkin(seq[1:], cache)
    result = (matchings + next_motzkin) % 1000000
    cache[seq] = result
    return result


def get_matching_bp(bp: str) -> str:
    return {
        'A': 'U',
        'U': 'A',
        'G': 'C',
        'C': 'G'
    }[bp]
