from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./ros_edit/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq1 = f[0][1]
    seq2 = f[1][1]
    # seq1 = 'ABC'
    # seq2 = 'ADABC'
    print(levenshtein(seq1, seq2))


def levenshtein(seq1, seq2):
    oneago = None
    thisrow = list(range(1, len(seq2) + 1)) + [0]
    for x in range(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in list(range(len(seq2))):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
    return thisrow[len(seq2) - 1]

