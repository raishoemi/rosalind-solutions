from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./pmch/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    rna_sequence = f[0][1]
    a_count = rna_sequence.count('A')
    c_count = rna_sequence.count('C')
    perfect_matchings = 1
    for i in range(1, a_count + 1):
        perfect_matchings *= i
    for i in range(1, c_count + 1):
        perfect_matchings *= i
    print(perfect_matchings)
    with open('./pmch/solution', 'w') as f:
        f.write(str(perfect_matchings))
