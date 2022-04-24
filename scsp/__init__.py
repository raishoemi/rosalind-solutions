from lcsq import find_ssm


def solve():
    input_file = open('./scsp/input.txt', 'r')
    dnas = list(map(lambda s: s.strip(), input_file.readlines()))
    dna1 = dnas[0]
    dna2 = dnas[1]
    # dna1 = 'ATTTTTG'
    # dna2 = 'GTTTTTA'
    # dna1 = 'AGA'
    # dna2 = 'GCA'
    dna1 = 'ATCTGAT'
    dna2 = 'TGCATA'
    lcs = find_ssm(dna1, dna2)
    if len(dna1) > len(dna2):
        shorter_dna = dna2
        longer_dna = dna1
    else:
        shorter_dna = dna1
        longer_dna = dna2

    scs = lcs
    shorter_dna_last_lcs_index = 0
    longer_dna_last_lcs_index = 0
    scs_additions = 0
    for i in range(len(lcs)):
        for j in range(shorter_dna_last_lcs_index, len(shorter_dna)):
            if shorter_dna[j] == lcs[i]:
                shorter_dna_last_lcs_index = j + 1
                break
            else:
                scs = scs[:i + scs_additions] + shorter_dna[j] + scs[i + scs_additions:]
                scs_additions += 1
         
        for j in range(longer_dna_last_lcs_index, len(longer_dna)):
            if longer_dna[j] == lcs[i]:
                longer_dna_last_lcs_index = j + 1
                break
            else:
                scs = scs[:i + scs_additions] + longer_dna[j] + scs[i + scs_additions:]
                scs_additions += 1

    if len(longer_dna) == len(shorter_dna):
        scs += shorter_dna[shorter_dna_last_lcs_index:]
    scs += longer_dna[longer_dna_last_lcs_index:]
         

    print(scs)
    print(len(scs))
