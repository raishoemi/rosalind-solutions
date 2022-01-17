from typing import List
from utils import get_uniprot_sequence


def solve():
    input_file = open('./mprt/input.txt', 'r')
    proteins = input_file.read().split('\n')
    input_file.close()
    motif_results = {}
    for protein_name in proteins:
        protein_sequence = get_uniprot_sequence(protein_name)
        motif_indicies = find_n_glycosylation_motifs(protein_sequence)
        if motif_indicies:
            motif_results[protein_name] = ' '.join([str(m) for m in motif_indicies])
    output_file = open('./mprt/test.output', 'w')
    for protein_name, motif_indicies in motif_results.items():
        output_file.write(f'{protein_name}\n')
        output_file.write(f'{motif_indicies}\n')

def find_n_glycosylation_motifs(protein_sequence: str) -> List[int]:
    n_glycosylation_motif_length = 4
    motif_indicies = []
    for i in range(len(protein_sequence) - n_glycosylation_motif_length + 1):
        if protein_sequence[i] == 'N':
            if protein_sequence[i + 1] != 'P':
                if protein_sequence[i + 2] == 'S' or protein_sequence[i + 2] == 'T':
                    if protein_sequence[i + 3] != 'P':
                        motif_indicies.append(i + 1)
    return motif_indicies

