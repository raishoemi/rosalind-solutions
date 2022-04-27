def solve():
    f = open('./conv/input.txt', 'r')
    lines = f.readlines()
    f.close()
    s1 = list(map(float, lines[0].strip().split()))
    s2 = list(map(float, lines[1].strip().split()))
    d = {}
    for n1 in s1:
        for n2 in s2:
            sub = abs(n1 - n2)
            found = False
            for key in d.keys():
                if abs(sub - key) < 0.01:
                    d[key] += 1
                    found = True
                    break
            if not found:
                d[sub] = 1
    max_multiplicity = 0
    x = 0
    for key, value in d.items():
        if value > max_multiplicity:
            max_multiplicity = value
            x = key
    print(max_multiplicity)
    print(x)

