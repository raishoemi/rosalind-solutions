def solve():
    s = 'CTAAGTCCTAAGTCGCTAAGTCGACTAAGTCCTAAGTCCTAAGTCCTAAGTCCCCTAAGTCCGTCACTAAGTCTCCTAAGTCAACTAAGTCGAACACTAAACTAAGTCGTACAAGGATACCAATTATACTAAGTCCACGATACTAAGTCCTCACACGCTAAGTCCTAAGTCCTAAGTCTGATCCTAAGTCTCTAAGTCTCTAAGTCTCTCACTAAGTCCTAAGTCCGCTAAGTCCTAAGTCCTAAGTCCTAAGTCGGACTAAGTCTCTAAGTCAGACACTAAGTCACTAAGTCCATAGGGTCTTAGGACCTAAGTCCTAAGTCCTAAGTCCTAAGTCCGGCTAAGTCTGACTAAGTCCCTAAGTCACTAGGAGGCTAAGTCTCTAAGTCCTATCGCACTAAGTCCTAAGTCTCTAAGTCAGTGTCTAAGTCCTCTAAGTCCTAAGTCCATCATCTCTAAGTCCTAAGTCCTAAGTCCTTGATCCTAAGTCCTAAGTCTCTAAGTCTTATTTTCTAAGTCCGACTCCTAAGTCCTAAGTCCTAAGTCGTAGCCAGCTAAGTCCTAACTGGCTAAGTCCGCTCTAAGTCCTAAGTCATTCCTAAGTCGCTAAGTCCTAAGTCAGCTCTCTAAGTCCGAACTAGTCCCCTAAGTCCTGACTAAGTCGATAACTAAGTCCTAAGTCCTAAGTCCTAAGTCCCTAAGTCTTTACTAAGTCTTGCTAAGTCCATGCTCTAAGTCTGCCTAAGTCCTAAGTCACTAAGTCTCCAAAGCTAAGTCGACAGCTAAGTCTCTAAGTCGCCGACTAAGTCTAACTAAGTCCCACTAAGTCCAGCGCTGCTAAGTCGCTAAGTCCCTAAGTCCTAAGTCGCTAAGTCGACGGGTTCCCCCCTAAGTCGTCGGTCTAAGTCCTAAGTCTCGCTAAGTCTTCCCTAAGTCCTTAGACTAAGTCTCTAAGTC'
    t = 'CTAAGTCCT'
    indicies = []
    start_at = 0
    while s.find(t, start_at) != -1:
        substring_index = s.find(t, start_at)
        indicies.append(substring_index + 1)
        start_at = substring_index + 1
    print(' '.join([str(i) for i in indicies]))