from io import StringIO
from Bio import Phylo

"""
Note, this solution counts trace length instead of just using the distance between the two nodes,
because the input trees provided by rosalind have `branch_length=0` and I could not find a way to
set it to 1 by default (when using BioPython to parse the tree).
"""

def solve():
    input_file = open('./nwck/input.txt', 'r')
    unparsed_trees = [[]]
    for line in input_file.readlines():
        if line == '\n':
            unparsed_trees.append([])
        else:
            unparsed_trees[-1].append(line.strip())
    input_file.close()
    distances = []
    for t in unparsed_trees:
        tree_str = t[0]
        distance_node1, distance_node2 = t[1].split()
        tree = Phylo.read(StringIO(tree_str), 'newick')
        distance_trace = tree.trace(distance_node1, distance_node2)
        distance = 1
        for clade in distance_trace:
            if clade.name != distance_node1 and clade.name != distance_node2:
                distance += 1
        distances.append(distance)
    print(' '.join(map(str, distances)))
