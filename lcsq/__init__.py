from Bio.SeqIO.FastaIO import SimpleFastaParser
from tqdm import tqdm
from itertools import combinations


def solve():
    input_file = open('./lcsq/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq1 = f[0][1]
    seq2 = f[1][1]
    if len(seq1) > len(seq2):
        smaller_seq = seq2
        larger_seq = seq1
    else:
        smaller_seq = seq1
        larger_seq = seq2
    index_map = {
        'A': [],
        'T': [],
        'C': [],
        'G': []
    }
    for i in range(len(larger_seq)):
        index_map[larger_seq[i]].append(i)

    print(lcs(index_map, smaller_seq, 0, True))

    lcs_candidates = []
    for i in tqdm(range(len(smaller_seq))):
        start_index = 0
        n = smaller_seq[i]
        candidate = n
        n_indicies = index_map[n]
        start_index = min(n_indicies) + 1
        for j in range(i+1, len(smaller_seq)):
            m = smaller_seq[j]
            m_indicies = index_map[m]
            try:
                start_index = min(
                    filter(lambda _: start_index <= _, m_indicies)) + 1
                candidate += m
            except ValueError:
                break
        lcs_candidates.append(candidate)

    # max_len_lcs = 0
    # lcs = ''
    # for s in lcs_candidates:
    #     s_len = len(s)
    #     if s_len > max_len_lcs:
    #         max_len_lcs = s_len
    #         lcs = s
    # print(lcs)


def lcs(index_map, s, start_index=0, first_run=False):
    if len(s) == 0:
        return ''
    n = s[0]
    n_indicies = index_map[n]
    try:
        start_index = min(filter(lambda _: _ >= start_index, n_indicies)) + 1
        if len(s) == 1:
            return n
    except ValueError:
        return ''
    lcs_candidates = []
    for i in range(1, len(s)):
        if first_run:
            print(i)
        m = s[i:]
        lcs_candidates.append(lcs(index_map, m, start_index))
    return n + max(lcs_candidates, key=len)
