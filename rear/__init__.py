from tqdm import tqdm


def solve():
    input = parse_input()
    results = []
    for source, target in input[:-1]:
        candidates = []
        cache = {}
        for reversal1 in tqdm(generate_reversals(source, target)):
            if str(reversal1) in cache:
                candidates.append(cache[str(reversal1)])
                continue
            if reversal1 == source:
                candidates.append(1)
                break
            for reversal2 in generate_reversals(source, reversal1):
                if str(reversal2) in cache:
                    candidates.append(cache[str(reversal2)])
                    continue
                if reversal2 == source:
                    candidates.append(2)
                    break
                for reversal3 in generate_reversals(source, reversal2):
                    if str(reversal3) in cache:
                        candidates.append(cache[str(reversal3)])
                        continue
                    if reversal3 == source:
                        candidates.append(3)
                        break
                    for reversal4 in generate_reversals(source, reversal3):
                        if str(reversal4) in cache:
                            candidates.append(cache[str(reversal4)])
                            continue
                        if reversal4 == source:
                            candidates.append(4)
                            break
                        for reversal5 in generate_reversals(source, reversal4):
                            if str(reversal5) in cache:
                                candidates.append(cache[str(reversal5)])
                                continue
                            if reversal5 == source:
                                candidates.append(5)
                                break
                            for reversal6 in generate_reversals(source, reversal5):
                                if str(reversal6) in cache:
                                    candidates.append(cache[str(reversal6)])
                                    continue
                                if reversal6 == source:
                                    candidates.append(6)
                                    break
                                for reversal7 in generate_reversals(source, reversal6):
                                    if str(reversal7) in cache:
                                        candidates.append(cache[str(reversal7)])
                                        continue
                                    if reversal7 == source:
                                        candidates.append(7)
                                        break
                                    for reversal8 in generate_reversals(source, reversal7):
                                        if str(reversal8) in cache:
                                            candidates.append(cache[str(reversal8)])
                                            continue
                                        if reversal8 == source:
                                            candidates.append(8)
                                            break
                                        for reversal9 in generate_reversals(source, reversal8):
                                            if str(reversal9) in cache:
                                                candidates.append(cache[str(reversal9)])
                                                continue
                                            if reversal9 == source:
                                                candidates.append(9)
                                                break
        if candidates == []:
            results.append(0)
        else:
            results.append(min(candidates))
    print(' '.join(map(str, results)))


def reversal_distance(source, target, max_depth, cache={}, first_call=False):
    if str((source, target)) in cache:
        return cache[str((source, target))], cache
    if source == target:
        return 0, cache
    if max_depth == 0:
        return len(source), cache
    reversal_distances = []
    for reversal in generate_reversals(source, target):
        distance, new_cache = reversal_distance(source, reversal, max_depth - 1, cache)
        reversal_distances.append(1 + distance)
        cache = {**cache, **new_cache}
    min_distance = min(reversal_distances)
    cache[str((source, target))] = min_distance
    return min_distance, cache


def generate_reversals(source, target):
    reversals = []
    for i in range(len(target)):
        if source[i] != target[i]:
            j = target.index(source[i])
            if i > j:
                reversals.append(target[:j] + list(reversed(target[j:i+1])) + target[i+1:])
            else:
                reversals.append(target[:i] + list(reversed(target[i:j+1])) + target[j+1:])
    return reversals

def parse_input():
    f = open('./rear/input.txt', 'r')
    lines = f.read().split('\n')
    f.close()
    input = [[]]
    for line in lines:
        if line != '':
            input[-1].append(line.split())
        else:
            input.append([])
    return input
