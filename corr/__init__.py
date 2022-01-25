from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio.Seq import Seq


def solve():
    input_file = open('./corr/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    incorrect_sequences = []
    correct_sequences = []
    correct_dups = 0
    for _, seq in f:
        if seq in correct_sequences or Seq(seq).reverse_complement() in correct_sequences:
            correct_dups += 1
            continue
        elif seq in incorrect_sequences:
            correct_sequences.append(seq)
            incorrect_sequences.remove(seq)
        elif Seq(seq).reverse_complement() in incorrect_sequences:
            correct_sequences.append(seq)
            incorrect_sequences.remove(Seq(seq).reverse_complement())
        else:
            incorrect_sequences.append(seq)
    print(correct_dups)
    matched_incorrect_sequences = []
    for incorrect_seq in incorrect_sequences:
        for correct_seq in correct_sequences:
            distance = 0
            for i in range(len(correct_seq)):
                if correct_seq[i] != incorrect_seq[i]:
                    distance += 1
                if distance > 1:
                    break
            if distance == 1:
                matched_incorrect_sequences.append(f'{incorrect_seq}->{correct_seq}')
                break
            else:
                distance = 0
                for i in range(len(correct_seq)):
                    if incorrect_seq[i] != Seq(correct_seq).reverse_complement()[i]:
                        distance += 1
                    if distance > 1:
                        break
                if distance == 1:
                    matched_incorrect_sequences.append(f'{incorrect_seq}->{Seq(correct_seq).reverse_complement()}')
                    break
    with open('corr/output.txt', 'w') as output_file:
        for s in matched_incorrect_sequences:
            output_file.write(f'{s}\n')
