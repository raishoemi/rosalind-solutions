from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio.Seq import Seq


def solve():
    input_file = open('./splc/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    dna = f[0][1]
    for i in range(1, len(f)):
        dna = dna.replace(f[i][1], '')
    print(Seq(dna).translate())
