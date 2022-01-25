from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./pdst/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    sequences = list(map(lambda fasta: fasta[1], f))
    result_matrix = []
    for i in range(len(sequences)):
        a = []
        for j in range(len(sequences)):
            a.append(0.0)
        result_matrix.append(a)
    for i in range(len(sequences) - 1):
        for j in range(i + 1, len(sequences)):
            hamming = get_hamming_ratio(sequences[i], sequences[j])
            result_matrix[i][j] = hamming
            result_matrix[j][i] = hamming
    for a in result_matrix:
        print(' '.join(map(lambda f: '{0:.4f}'.format(f), a)))
    with open('./pdst/solution', 'w') as f:
        for a in result_matrix:
            f.write(' '.join(map(lambda f: '{0:.4f}'.format(f), a)))
            f.write('\n')

def get_hamming_ratio(s1, s2):
    d = 0
    for _ in range(len(s1)):
        if s1[_] != s2[_]:
            d += 1
    return d / len(s1)
