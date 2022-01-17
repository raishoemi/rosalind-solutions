from typing import List
from Bio.SeqIO.FastaIO import SimpleFastaParser
from difflib import SequenceMatcher
from tqdm import tqdm

def solve():
    input_file = open('./lscm/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    lcs = ''
    best_lcs_len = 0
    for i in tqdm(range(len(f))):
        fasta1_name, fasta1_seq = f[i][0], f[i][1]
        current_fasta_lcs = ''
        all_substrings = sorted(get_all_substrings(fasta1_seq, best_lcs_len), key=len)
        all_substrings.reverse()
        for substring in all_substrings:
            is_common = True
            for fasta2_name, fasta2_seq in f:
                if fasta1_name != fasta2_name:
                    if substring not in fasta2_seq:
                        is_common = False
                        break
            if is_common:
                current_fasta_lcs = substring
                break
        if len(current_fasta_lcs) > best_lcs_len:
            lcs = current_fasta_lcs
            best_lcs_len = len(lcs)
    print(lcs)

def get_all_substrings(s: str, min_length: int) -> List[str]:
    substrings = []
    if min_length == 0:
        min_length = 1
    for i in range(len(s)):
        for j in range(i + min_length, len(s) + 1):
            substrings.append(s[i:j])
    return substrings
