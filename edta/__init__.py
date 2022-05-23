from re import L
from Bio.SeqIO.FastaIO import SimpleFastaParser
from lcsq import find_ssm


def solve():
    input_file = open('./edta/input.txt', 'r')
    f = list(SimpleFastaParser(input_file))
    input_file.close()
    seq1 = f[0][1]
    seq2 = f[1][1]
    print(seq1)
    print(seq2)
    l = levenshtein(seq1, seq2)
    print(l)
    for r in l:
        print(r)
    with open('./edta/output.txt', 'w') as f:
        f.write(str(l[0]) + '\n')
        f.write(str(l[1]) + '\n')
        f.write(str(l[2]) + '\n')
    
def levenshtein(s1, s2):
    rows = []
    for i in range(len(s1) + 1):
        rows.append([])
        for j in range(len(s2) + 1):
            rows[i].append(0)

    for i in range(1, len(s1) + 1):
        rows[i][0] = (i, s1[:i], '-' * i)
    for i in range(1, len(s2) + 1):
        rows[0][i] = (i, '-' * i, s2[:i])
    rows[0][0] = (0, '', '')

    # for row in rows:
    #     print(row)
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            s1_prefix = rows[i-1][j]
            s2_prefix = rows[i][j-1]
            s1_s2_prefix = rows[i-1][j-1]
            if s1_prefix[0] + 1 <= s2_prefix[0] + 1 and s1_prefix[0] + 1 <= s1_s2_prefix[0] + substitution_cost:
                rows[i][j] = (s1_prefix[0] + 1, s1_prefix[1] + s1[i-1], s1_prefix[2] + '-')
            elif s2_prefix[0] + 1 <= s1_prefix[0] + 1 and s2_prefix[0] + 1 <= s1_s2_prefix[0] + substitution_cost:
                rows[i][j] = (s2_prefix[0] + 1, s2_prefix[1] + '-', s2_prefix[2] + s2[j-1])
            else:
                rows[i][j] = (s1_s2_prefix[0] + substitution_cost, s1_s2_prefix[1] + s1[i-1], s1_s2_prefix[2] + s2[j-1])
            # rows[i][j] = min(rows[i-1][j] + 1, rows[i][j-1] + 1, rows[i-1][j-1] + substitution_cost)
    
    # for row in rows:
    #     print(row)
    return rows[len(s1)][len(s2)]


def levenshtein_rec(s1 ,s2, cache={}):
    if (s1, s2) in cache:
        print('cache hit')
        return cache[(s1, s2)], cache
    if len(s1) == 0:
        cache[(s1, s2)] = len(s2), '-' * len(s2), s2
        return cache[(s1, s2)], cache
    elif len(s2) == 0:
        cache[(s1, s2)] = len(s1), s1, '-' * len(s1)
        return cache[(s1, s2)], cache
    elif s1[0] == s2[0]:
        l, new_cache = levenshtein_rec(s1[1:], s2[1:])
        cache = {**cache, **new_cache}
        return (l[0], s1[0] + l[1], s2[0] + l[2]), cache
    else:
        l1_tail, new_cache = levenshtein_rec(s1[1:], s2)
        cache = {**cache, **new_cache}
        l2_tail, new_cache = levenshtein_rec(s1, s2[1:])
        cache = {**cache, **new_cache}
        l1_l2_tail, new_cache = levenshtein_rec(s1[1:], s2[1:])
        cache = {**cache, **new_cache}
        if l1_tail[0] <= l2_tail[0] and l1_tail[0] <= l1_l2_tail[0]:
            return (l1_tail[0] + 1, s1[0] + l1_tail[1], '-' + l1_tail[2]), cache
        if l2_tail[0] <= l1_tail[0] and l2_tail[0] <= l1_l2_tail[0]:
            return (l2_tail[0] + 1, '-' + l2_tail[1], s2[0] + l2_tail[2]), cache
        if l1_l2_tail[0] <= l2_tail[0] and l1_l2_tail[0] <= l1_tail[0]:
            return (l1_l2_tail[0] + 1, s1[0] + l1_l2_tail[1], s2[0] + l1_l2_tail[2]), cache
