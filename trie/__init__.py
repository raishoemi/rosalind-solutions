def solve():
    f = open('./trie/input2.txt')
    lines = list(map(lambda x: x.strip(), f.readlines()))
    f.close()
    results = []
    last_index = 1
    for i in range(len(lines)):
        results.append([])
        matching_lines = list(filter(lambda x: len(
            x) > 0 and x[0][0] == lines[i][0], results))
        matching_line = matching_lines[0] if len(matching_lines) > 0 else None
        for j in range(len(lines[i])):
            if matching_line:
                if matching_line[j][0] != lines[i][j]:
                    new_matching_line = find_matching_sequence(results, matching_line[j-1][2], lines[i][j])
                    if new_matching_line:
                        matching_line = matching_line[:j] + new_matching_line
                    else:
                        last_index += 1
                        results[-1].append((lines[i][j], matching_line[j]
                                    [1], last_index))
                        matching_line = None
            else:
                if j == 0:
                    last_index += 1
                    results[-1].append((lines[i][j], 1, last_index))
                else:
                    results[-1].append((lines[i][j], last_index, last_index + 1))
                    last_index += 1

    s = ''
    for arr in results:
        for item in arr:
            s += f'{item[1]} {item[2]} {item[0]}\n'
    f = open('./trie/output.txt', 'w')
    f.write(s)
    f.close()
    print(s)

def find_matching_sequence(results, last_matching_item_index, current_char):
    for i in range(len(results)):
        for item in results[i]:
            if item[1] == last_matching_item_index and item[0] == current_char:
                return results[i]
    return None
