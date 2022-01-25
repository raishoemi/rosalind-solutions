from itertools import permutations
from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./kmer/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq = f[0][1]
    kmer_dict = { ''.join(p): 0 for p in sorted(set(permutations(['A', 'C', 'G', 'T'] * 4, 4))) }
    for i in range(len(seq) - 3):
        kmer_dict[seq[i:i+4]] += 1
    result = ''
    for _, count in kmer_dict.items():
        result += str(count) + ' '
    with open('kmer/output.txt', 'w') as output_file:
        output_file.write(result)
