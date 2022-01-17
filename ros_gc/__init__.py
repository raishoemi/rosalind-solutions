def solve():
    input_file = open('./ros_gc/input', 'r')
    lines = input_file.readlines()
    input_file.close()
    samples = []
    contents = []
    for line in lines:
        if line.startswith('>Rosalind'):
            samples.append(line.strip()[1:])
            contents.append('')
        else:
            contents[-1] += line.strip()
    max_gc = 0
    highest_gc_sample = ''
    for i in range(len(samples)):
        gc_percentage = ((contents[i].count('G') + contents[i].count('C')) / len(contents[i])) * 100
        if gc_percentage > max_gc:
            highest_gc_sample = samples[i]
            max_gc = gc_percentage
    print(highest_gc_sample)
    print(max_gc)
