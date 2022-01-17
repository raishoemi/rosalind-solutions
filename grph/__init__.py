from Bio.SeqIO.FastaIO import SimpleFastaParser

def solve():
    input_file = open('./grph/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    k = 3
    for fasta1_name, fasta1_seq in f:
        for fasta2_name, fasta2_seq in f:
            if fasta1_name != fasta2_name:
                if fasta1_seq[-k:] == fasta2_seq[:k]:
                    print(f"{fasta1_name} {fasta2_name}")
