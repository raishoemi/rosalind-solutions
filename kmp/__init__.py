from Bio.SeqIO.FastaIO import SimpleFastaParser
from functools import lru_cache
from tqdm import tqdm
from math import ceil


def solve():
    input_file = open('./kmp/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq = f[0][1]
    seq_len = len(seq)
    failure_arr = [0] * seq_len 
    combos = []
    for i in tqdm(range(1, seq_len)):
        combo_indicies_to_remove = []
        found_higher = False
        for _ in range(len(combos)):
            if seq[i] == seq[combos[_]]:
                combos[_] += 1
                found_higher = True
                failure_arr[i] = combos[_]
            else:
                combo_indicies_to_remove.append(_)
        for j in range(len(combo_indicies_to_remove)):
            combo_index = combo_indicies_to_remove[j]
            combos.pop(combo_index - j)
        if seq[i] == seq[0]:
            combos.insert(0, 1)
            if not found_higher:
                failure_arr[i] = 1
    with open('kmp/output.txt', 'w') as output_file:
        for f in failure_arr:
            output_file.write(str(f) + ' ')

@lru_cache(maxsize=None)
def get_longest_failure_string(seq: str) -> str:
    seq_len = len(seq)
    max_substr_len = int(seq_len / 2)
    longest_failure_string = ''
    for i in range(1, max_substr_len):
        current_seq = seq[:i]
        if current_seq == seq[len(seq) - i:]:
            if len(seq[:i]) > len(longest_failure_string):
                longest_failure_string = current_seq
    return longest_failure_string
