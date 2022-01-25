def solve():
    input = parse_input()
    results = []
    for source, reversed_input in input:
        print(f'{source} => {reversed_input}')
        reverse_counter = 0
        for i in range(len(source)):
            if source[i] != reversed_input[i]:
                reversed_index = reversed_input.index(source[i])
                reversed_chunk = list(reversed(reversed_input[i:reversed_index+1]))
                reversed_input = reversed_input[:i] + reversed_chunk + reversed_input[reversed_index+1:]
                reverse_counter += 1
        results.append(reverse_counter)
    print(results)

    

def parse_input():
    f = open('./rear/sample', 'r')
    lines = f.read().split('\n')
    f.close()
    input = [[]]
    for line in lines:
        if line != '':
            input[-1].append(line.split())
        else:
            input.append([])
    return input
