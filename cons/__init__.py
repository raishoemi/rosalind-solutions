from Bio.SeqIO.FastaIO import SimpleFastaParser
def solve():
    input_file = open('./cons/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    profile_matrix = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
    }
    for j in range(len(f[0][1])):
        for key in profile_matrix.keys():
            profile_matrix[key].append(0)
        for i in range(len(f)):
            profile_matrix[f[i][1][j]][j] += 1
    consensus_string = ''
    for i in range(len(profile_matrix['A'])):
        max_value = 0
        max_key = ''
        for key in profile_matrix.keys():
            if profile_matrix[key][i] > max_value:
                max_value = profile_matrix[key][i]
                max_key = key
        consensus_string += max_key
    print(consensus_string)
    for key in profile_matrix:
        print(f"{key}: {' '.join(map(str, profile_matrix[key]))}")
