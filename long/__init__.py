from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./long/input.txt', 'r')
    fasta = list(SimpleFastaParser(input_file))
    fasta_dict = {k: v for k, v in fasta}
    input_file.close()
    pairs = []
    for fasta_1_name, fasta_1_seq in fasta:
        similarities = []
        for fasta_2_name, fasta_2_seq in fasta:
            if fasta_1_name == fasta_2_name:
                continue
            similarity, i = get_similarity(fasta_1_seq, fasta_2_seq)
            if similarity and similarity > 50:
                similarities.append((fasta_1_name, fasta_2_name, i, similarity))
        if similarities == []:
            print('No similar sequences found for {}'.format(fasta_1_name))
            continue
        most_similar_pair = max(similarities, key=lambda x: x[3])
        pairs.append((most_similar_pair[0], most_similar_pair[1], most_similar_pair[2]))
    print(pairs)

    # for fasta_name in fasta_dict:
    #     if not any(fasta_name == pair[0] for pair in pairs):
    #         print(f'Could not find pair for {fasta_name} (might be last one)')
    #     if not any(fasta_name == pair[1] for pair in pairs):
    #         print(f'Could not find pair for {fasta_name} (might be last one)')


    first_pair = None
    for pair in pairs:
        is_first_pair = True
        for pair2 in pairs:
            if pair[0] != pair2[0] and pair[0] == pair2[1]:
                is_first_pair = False
                break
        if is_first_pair:
            first_pair = pair
            break
    print(first_pair)

    final_seq = ''
    hops = 0
    while first_pair:
        hops += 1
        final_seq += fasta_dict[first_pair[0]][:first_pair[2]]
        next_pair = None
        for pair in pairs:
            if pair[0] == first_pair[1]:
                next_pair = pair
                break
        if not next_pair:
            final_seq += fasta_dict[first_pair[1]]
        first_pair = next_pair
        
    print(final_seq)
    print(hops)
    with open('./long/output.txt', 'w') as output_file:
        output_file.write(final_seq)


def get_similarity(seq1: str, seq2: str):
    len_diff = len(seq2) - len(seq1)
    original_seq1_len = len(seq1)
    if len_diff > 0:
        seq2 = seq2[:len(seq2) - len_diff]
        len_diff = 0
    elif len_diff < 0:
        len_diff = -len_diff
        seq1 = seq1[len_diff:]
    for i in range(len(seq2)):
        if seq2[:len(seq2) - i] == seq1[i:]:
            index = i + len_diff
            similarity = 100 * ((original_seq1_len - i) / original_seq1_len)
            return similarity, index
    return None, None
