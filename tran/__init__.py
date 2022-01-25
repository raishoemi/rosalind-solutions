from tkinter import W
from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./tran/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    s1 = f[0][1]
    s2 = f[1][1]
    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        both_purine = is_purine(s1[i]) and is_purine(s2[i])
        both_pyrimidine = not is_purine(s1[i]) and not is_purine(s2[i])
        if both_purine or both_pyrimidine:
            transitions += 1
        else:
            transversions += 1
    print(transitions / transversions)

def is_purine(nucleotide):
    return nucleotide == 'A' or nucleotide == 'G'
