from typing import List, Tuple
from Bio.Seq import Seq
from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./revp/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    dna = f[0][1]
    # dna = 'TCAATGCATGCGGGTCTATATGCAT'
    permutations = get_permutations(dna, 4, 12)
    print(permutations)
    palindromes = []
    for permutation, index in permutations:
        if permutation == Seq(permutation).reverse_complement():
            palindromes.append(f'{index + 1} {len(permutation)}')
    for p in palindromes:
        print(p)

def get_permutations(s: str, min_len: int, max_len: int) -> List[Tuple[str, int]]:
    permutations = []
    for i in range(len(s) - min_len + 1):
        for j in range(i + min_len, i + max_len + 1):
            if j > len(s):
                break
            permutations.append((s[i:j], i))
    return permutations
