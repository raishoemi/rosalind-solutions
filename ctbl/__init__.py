from io import StringIO
from Bio import Phylo


def solve():
    input_file = open('./ctbl/input.txt', 'r')
    tree_raw = input_file.read().strip()
    input_file.close()
    tree = Phylo.read(StringIO(tree_raw), 'newick')
    non_trivial_characters = get_non_trivial_characters(tree.clade)
    all_clades = list(sorted(map(lambda c: c.name, filter(lambda c: c.name != None ,tree.find_clades()))))
    results = []
    for arr in non_trivial_characters:
        results.append([])
        for clade in all_clades:
            if clade in arr:
                results[-1].append(1)
            else:
                results[-1].append(0)
    s = ''
    for r in results:
        s += ''.join(map(str, r)) + '\n'
    print(s)
    output_file = open('./ctbl/output.txt', 'w')
    output_file.write(s)
    output_file.close()


def get_non_trivial_characters(clade):
    non_trivial_characters = []
    if len(clade.clades) < 2:
        return []
    for current_clade in clade.clades:
        if current_clade.name == None:
            non_trivial_characters.append(list(map(lambda c: c.name, filter(lambda c: c.name != None, current_clade.find_clades()))))
            nested_non_trivial_characters = get_non_trivial_characters(current_clade)
            for arr in nested_non_trivial_characters:
                if len(arr) > 0:
                    non_trivial_characters.append(arr)
    return non_trivial_characters
