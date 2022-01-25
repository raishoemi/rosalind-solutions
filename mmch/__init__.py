from Bio.SeqIO.FastaIO import SimpleFastaParser


def solve():
    input_file = open('./mmch/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq = f[0][1]
    a_count = seq.count('A')
    u_count = seq.count('U')
    au_matchings = 1
    if a_count == u_count:
        for i in range(1, a_count + 1):
            au_matchings *= i
    else:
        for i in range(abs(a_count - u_count) + 1, max(a_count, u_count) + 1):
            au_matchings *= i
        
    c_count = seq.count('C')
    g_count = seq.count('G')
    cg_matchings = 1
    if c_count == g_count:
        for i in range(1, c_count + 1):
            cg_matchings *= i
    else:
        for i in range(abs(c_count - g_count) + 1, max(c_count, g_count) + 1):
            cg_matchings *= i
    print(au_matchings * cg_matchings)
    with open('./mmch/solution', 'w') as f:
        f.write(str(au_matchings * cg_matchings))
