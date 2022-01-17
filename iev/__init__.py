def solve():
    input_string = '17097 17478 19814 18468 17638 17215'
    groups = input_string.split(' ')
    colony_size = sum(map(int, groups)) * 2
    hetero_hetero = int(groups[3]) * 0.25 * 2
    hetero_homorec = int(groups[4]) * 0.5 * 2
    homorec_homorec = int(groups[5]) * 2
    rec_phenotype = hetero_hetero + hetero_homorec + homorec_homorec
    dom_phenotype = colony_size - rec_phenotype
    print(dom_phenotype)
