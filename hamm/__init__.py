def solve():
    input_file = open('./hamm/input.txt', 'r')
    lines = input_file.readlines()
    input_file.close()
    dna1 = lines[0].strip()
    dna2 = lines[1].strip()
    d = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            d += 1
    print(d)
