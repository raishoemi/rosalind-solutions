from Bio.Seq import Seq


def solve():
    input_file = open('./dbru/input.txt', 'r')
    lines = input_file.readlines()[:-1]
    input_file.close()
    sequences = list(map(lambda l: l.strip(), lines))
    reverse_complements = list(map(lambda s: str(Seq(s).reverse_complement()), sequences))
    
    k_mers = set()
    for s in sequences:
        k_mers.add(s)
    for s in reverse_complements:
        k_mers.add(s)
    results = set()
    for k_mer in k_mers:
        if ((k_mer[1:], k_mer[:1]) in results):
            continue
        results.add((k_mer[:-1], k_mer[1:]))
    with open('./dbru/output.txt', 'w') as output_file:
        for r in results:
            output_file.write(f'({r[0]}, {r[1]})\n')
