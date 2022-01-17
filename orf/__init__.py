from Bio.Data.CodonTable import standard_dna_table
from Bio.Seq import Seq
from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./orf/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    dna = f[0][1]
    reverse_dna = Seq(dna).reverse_complement()
    protein_candidates = get_protein_candidates(dna)
    protein_candidates.extend(get_protein_candidates(reverse_dna))
    protein_candidates = list(set(protein_candidates))
    for protein in protein_candidates:
        print(protein)
    
def get_protein_candidates(dna):
    protein_candidates = []
    start_index = 0
    while start_index < len(dna) - 6:
        if dna[start_index:start_index + 3] == 'ATG':
            current_protein = 'M'
            for end_index in range(start_index + 3, len(dna) - 3, 3):
                codon = dna[end_index:end_index + 3]
                if codon in standard_dna_table.stop_codons:
                    protein_candidates.append(current_protein)
                    break
                else:
                    current_protein += standard_dna_table.forward_table[codon]
        start_index += 1
    return protein_candidates
