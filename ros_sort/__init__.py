from tqdm import tqdm


def solve():
    input = parse_input()
    results = []
    for target, source in input[:-1]:
        candidates = {}
        cache = {}
        for reversal1, reversal1_indicies in tqdm(generate_reversals(source, target)):
            if str(reversal1) in cache:
                candidates.append(cache[str(reversal1)])
                continue
            if reversal1 == source:
                candidates[1] = [reversal1_indicies]
                break
            for reversal2, reversal2_indicies in generate_reversals(source, reversal1):
                if str(reversal2) in cache:
                    candidates.append(cache[str(reversal2)])
                    continue
                if reversal2 == source:
                    candidates[2] = [reversal1_indicies, reversal2_indicies]
                    break
                for reversal3, reversal3_indicies in generate_reversals(source, reversal2):
                    if str(reversal3) in cache:
                        candidates.append(cache[str(reversal3)])
                        continue
                    if reversal3 == source:
                        candidates[3] = [reversal1_indicies,
                                         reversal2_indicies, reversal3_indicies]
                        break
                    for reversal4, reversal4_indicies in generate_reversals(source, reversal3):
                        if str(reversal4) in cache:
                            candidates.append(cache[str(reversal4)])
                            continue
                        if reversal4 == source:
                            candidates[4] = [
                                reversal1_indicies, reversal2_indicies, reversal3_indicies, reversal4_indicies]
                            break
                        for reversal5, reversal5_indicies in generate_reversals(source, reversal4):
                            if str(reversal5) in cache:
                                candidates.append(cache[str(reversal5)])
                                continue
                            if reversal5 == source:
                                candidates[5] = [reversal1_indicies, reversal2_indicies,
                                                 reversal3_indicies, reversal4_indicies, reversal5_indicies]
                                break
                            for reversal6, reversal6_indices in generate_reversals(source, reversal5):
                                if str(reversal6) in cache:
                                    candidates.append(cache[str(reversal6)])
                                    continue
                                if reversal6 == source:
                                    candidates[6] = [reversal1_indicies, reversal2_indicies, reversal3_indicies,
                                                     reversal4_indicies, reversal5_indicies, reversal6_indices]
                                    break
                                for reversal7, reversal7_indicies in generate_reversals(source, reversal6):
                                    if str(reversal7) in cache:
                                        candidates.append(
                                            cache[str(reversal7)])
                                        continue
                                    if reversal7 == source:
                                        candidates[7] = [reversal1_indicies, reversal2_indicies, reversal3_indicies,
                                                         reversal4_indicies, reversal5_indicies, reversal6_indices, reversal7_indicies]
                                        break
                                    for reversal8, reversal8_indicies in generate_reversals(source, reversal7):
                                        if str(reversal8) in cache:
                                            candidates.append(
                                                cache[str(reversal8)])
                                            continue
                                        if reversal8 == source:
                                            candidates[8] = [reversal1_indicies, reversal2_indicies, reversal3_indicies, reversal4_indicies,
                                                             reversal5_indicies, reversal6_indices, reversal7_indicies, reversal8_indicies]
                                            break
                                        for reversal9, reversal9_indicies in generate_reversals(source, reversal8):
                                            if str(reversal9) in cache:
                                                candidates.append(cache[str(reversal9)])
                                                    
                                                continue
                                            if reversal9 == source:
                                                candidates[9]=[reversal1_indicies, reversal2_indicies, reversal3_indicies, reversal4_indicies,
                                                                 reversal5_indicies, reversal6_indices, reversal7_indicies, reversal8_indicies, reversal9_indicies]
                                                break
        if len(candidates.keys()) == 0:
            print('NO REVERSALS NEEDED')
        else:
            for i in range(1, 11):
                if i in candidates:
                    print(i)
                    for i, j in candidates[i]:
                        print(i + 1, j + 1)
                    break


def reversal_distance(source, target, max_depth, cache={}, first_call=False):
    if str((source, target)) in cache:
        return cache[str((source, target))], cache
    if source == target:
        return 0, cache
    if max_depth == 0:
        return len(source), cache
    reversal_distances = []
    for reversal in generate_reversals(source, target):
        distance, new_cache = reversal_distance(
            source, reversal, max_depth - 1, cache)
        reversal_distances.append(1 + distance)
        cache={**cache, **new_cache}
    min_distance=min(reversal_distances)
    cache[str((source, target))]=min_distance
    return min_distance, cache


def generate_reversals(source, target):
    reversals=[]
    for i in range(len(target)):
        if source[i] != target[i]:
            j=target.index(source[i])
            if i > j:
                reversals.append(
                    (target[:j] + list(reversed(target[j:i+1])) + target[i+1:], (i, j)))
            else:
                reversals.append(
                    (target[:i] + list(reversed(target[i:j+1])) + target[j+1:], (i, j)))

    return reversals


def parse_input():
    f=open('./ros_sort/input.txt', 'r')
    lines=f.read().split('\n')
    f.close()
    input=[[]]
    for line in lines:
        if line != '':
            input[-1].append(line.split())
        else:
            input.append([])
    return input
