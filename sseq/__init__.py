from Bio.SeqIO.FastaIO import SimpleFastaParser

def solve():
    input_file = open('./sseq/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq = f[0][1]
    sub_sequence = f[1][1]
    indicies = []
    for nucleotide in sub_sequence:
        last_index = 0 if indicies == [] else indicies[-1]
        indicies.append(seq.index(nucleotide, last_index) + 1)
    print(' '.join(map(str, indicies)))
