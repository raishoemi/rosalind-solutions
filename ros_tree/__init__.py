def solve():
    f = open('./ros_tree/input.txt', 'r')
    lines = f.readlines()
    f.close()
    n = int(lines[0])
    edges = []
    for i in range(1, len(lines)):
        edges.append(list(map(int, lines[i].split())))
    print(n - len(edges) - 1)
