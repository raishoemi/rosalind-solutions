from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./lcsq/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq1 = f[0][1]
    seq2 = f[1][1]
    print(find_ssm(seq1, seq2))

def find_ssm(DNA1, DNA2):
    mainlst = []
    for _ in range(len(DNA1)+1):
        lst = []
        mainlst.append(lst)
        for _ in range(len(DNA2)+1):
            lst.append(0)
    for i in range(1, len(DNA1)+1):
        for j in range(1, len(DNA2)+1):
            if DNA1[i-1] == DNA2[j-1]:
                mainlst[i][j] = mainlst[i-1][j-1]+1
            else:
                mainlst[i][j] = max(mainlst[i-1][j], mainlst[i][j-1])

    m, n, lcmq = len(DNA1), len(DNA2), ''
    while mainlst[m][n] != 0:

        if mainlst[m][n] == mainlst[m-1][n]:
            m -= 1
        elif mainlst[m][n] == mainlst[m][n-1]:
            n -= 1
        else:
            lcmq += DNA1[m-1]
            m -= 1
            n -= 1
    lcmq = list(lcmq)
    lcmq.reverse()
    lcmq = ''.join(lcmq)
    return lcmq