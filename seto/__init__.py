from utils import parse_set


def solve():
    f = open('./seto/input.txt', 'r')
    lines = f.readlines()
    f.close()

    n = lines[0]
    a = set(map(int, parse_set(lines[1])))
    b = set(map(int ,parse_set(lines[2])))
    output = ''
    output += str(a.union(b)) + '\n'
    output += str(a.intersection(b)) + '\n'
    output += str(a.difference(b)) + '\n'
    output += str(b.difference(a)) + '\n'
    output += str(set(range(1, int(n) + 1)) - a) + '\n'
    output += str(set(range(1, int(n) + 1)) - b)
    f = open('./seto/output.txt', 'w')
    f.write(output)
    f.close()
