from typing import List


def solve():
    n = 6
    options = generate_options(n)
    permutations = generate_permutations(options)
    print(len(permutations))
    print(permutations)
    with open('./sign/output.txt', 'w') as f:
        f.write(str(len(permutations)) + '\n')
        for permutation in permutations:
            f.write(' '.join(map(str, permutation)) + '\n')

def generate_options(n: int) -> List[int]:
    options = []
    for i in range(1, n + 1):
        options.append(i)
        options.append(-i)
    return options

def generate_permutations(options: List[int]) -> List[List[int]]:
    if len(options) == 2:
        return options
    permutations = []
    for option in options:
        options_excluding_current = options.copy()
        options_excluding_current.remove(option)
        options_excluding_current.remove(-option)
        for permutation in generate_permutations(options_excluding_current):
            if type(permutation) == int:
                permutations.append([option, permutation])
            else:
                permutations.append([option] + permutation)
    return permutations
