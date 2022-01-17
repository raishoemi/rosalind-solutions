from Bio.Seq import translate
def solve():
    rna = 'AUGGCCUCGAUAGCUCCGUCUGUUAUUUGCGUGUUAGACAUUUCUCUGGACCCUCAGGACGCGGUCCGGGCUGUACCGGAAACUUUGCCCGUAUUCGCUCCAGAACCUAGUCUAGGCUCACACUCAACAAGAAUGAACCGAUAUAGAGAAACACACAGGCUCCUCUUACGUGGGCUUGGAGAACUGCUUUUGAGCUGCGGGGCUCCCCCUCAAACCCACACUAAGAUCUUCAAUUUGUCUUCAGUCAGUUUCAUGGCUCAUUCACGGAAUCUUUCGAGCGACGUAUCAUUCGGCCUACUCUCUUGCCGUGAAGAGGUACAAGAGAGGACUCCGUCGUUCUGCGGGACGGGCGGUUUGCCAAUUGUACCUUGGGGCCACCGAGCGGCUACAGCGGACCCUUUCGAGAAACGGAGAGCAGUGUCUCAGUGUCUUCGAUGCUCGUCCUGCAUCGCUAUACGGCCGGCCUUUAUUGUUACGGAAAGCCGAGGUCGAUACAGUUCGACAACCAUGACCGGAUUAGGUGGAGACUGGCAAACAACGGCCCCCGAGCCAGAUGAUUUAAAGACCUUUACGCUCCACCUGGGGGUGGAGGAACAUGCCCUAUUGUCCACGGUGGUAGCGAUGCGGAUAAAUAACGUCAGAGAUCGCUUUAUACUCCGCACUAGCGAUUUCCCACGCUGUUGCUAUCUUAGAAAAUUACGAGGCUACACUAGGAAAAUUAGGCAACUGGCAAGCAUCUCCAACCUUGGUCGGAGCUCCUUAGGGCUCGUGUCAAUGUCCGGUGUAGACCCUACACCGGGAUAUACGUGCAGAACACGGUGCUGUAUAAAUCGUGUGCCCUAUUCAGUGCUACGAGCAAGAGCACAAAGUUGGAACCAACGGGGGCCCGACUGGGCACCGAUAGUUGUGUGCGGAGAAUUUCGGCGUGGCCUUAUAUCCCCGCGCGUCAAAGUGCUGCUGCAACCCGGGUUAGCACUUCUGUGCAUGGCUAGAGUCGAGUGCCGCCACCUACUUUGGUCUACAUAUUCCAUGAUAAACAAAGGCAAGAUGCUAAUGAUAAAUGGCGUCAGGCCGCAUGCCGGGUGUGUUAUCCGUAGACGUUACCUUGGCCAUGCAUUUGCUACGGUAGACGCGCCCGAGUUGACGUUCACACUCGAGACGUCACCAAAAAAAGAUAAGCCGCUGCUAGGGCAAGUCAAAUUUAAAUUCUUUGGACGGGGUGGACUCCACUUCCUUACCCCUGUUCGUGCGCCAUAUGCCUCAACAGUGUUAUACUUAAGACGCCUUCAGGGGGCCGUUCUCGCGCUUACAGGCGGUAGCCCACCCGUAACCUUGUGGCCUCCGCAAACCGAGCCAAUAUCUUCUCUAAGUGUAUUCUUAAGAGCGAUGGGGAUGCGUAUAGUCGGUCGGUCCCACGAACCACGGGCUAUCCUUGGCAAACUCCAGCGAUAUCAAUUUAAGGUCAUUUGCAGGAGAGAUGUCUUUCGUACGACCGCCCGAUACUACGCCAUGUGCCGCCGAGUCAGAUGGCGCAAAACCCAUGCAAACCCGCGGCAACGGUCUCACCUGGGGAAACCUUGUAUCCGUCCACCUUGCAGGAUGACCCGUGCGAGCUUCCCCCUCAAAUUUGUGGCGACGACAGCACGUGGACGCGCAGCUGACCAUAUCCAUGAGUUGGCACAAUGCCCAUCAGUGCGCCUAGUAAAACGAAAUCUGCACAGCAAGUACCCCUAUCAAGGACGGCUGUCCUCGAGCUUCCAAAAAGGUAUUUGUGAGCACAAACGCACGUCAAACAUGGACCCAGUGCUCCUCAGCAACCUACAGACGUUCCGGUCCCAACCAAGAUUAUGGUUUCUGUUUCAGUGUACCUGCUGUACCGAUCUUAUCUAUUCACCUGCGAAGCGGCUUCAUCAACUAUCUAUUAAGCCCACUAUCUUACUCGCCCGAGUGGCGUAUUUAUGCACUUACGUGGUAAAAAUCCUAUAUGUGAUUGAACAUAGAGUCCUACUGGGGAAUCAUUGGCAAAUAUGCCCGUUGGUGCAUCACUGGCGGCACCCACUGCACAGUCGUAGACUUAAUGCCCCGUGCGCCCUCUGCGAAUGGAAUUUUACAAAACAGCAUGGAGACCUGCCUAGCGCUUUCUCUCACGGUUCUAAUCCAGCAUUGGCGCGGAAACCUGUACAAUUUGGACCGCUACGAGAUAGAGAGAAAAACCCGCCUAACAACCGCUCUUGCUCGCAGACAGGUCCGACGGUCUCCAACAAGUUAGGCAGUAUGAGGAGGUUUCGCCCAGCAGAAACGUUCCAGAGACGAAUCAAGGAUCCGCGGAGCGCGAGUAUCCCACCGUUAGCAACGCUGGGUCUGAGCUUCUUGAGUAGUCGAGCAGAAUGUCAUCCAACAAAGGUGCCAAGCAUCCCCUGCUUGAUUCCUCAAGGUUCAUUGUCAACAAUCUCCAGCAUCUGGCGCCAUACAAGUGUGGCUUCGCAAAGAUCUACACACGACGGCCAUUUUGAUCGACACCUCAGGGAGCUGGGCACUCCUCAACCCUGGGGAAGAUUAAGAGACUUAUCACCAGCUCACCAACGCGGAUACAGAUCAUGUAAAUUGGAGCGUAGUGAACCGUACCGACUUUGUAGUGAUAUUCUAUUCAAUGAAACUGCCGCCUUUAUACAUUCUAAGGUUCACCCUCGUUCCGUGUCUAGUUCCCUCGUCAUCCAUUACUAUUCUAUACCCGUACUACGCACCGGGGCGUCUCUGCUCGCCCGACAAUAUAAUAAGCUUCCUCUACUUGCAGUGUGUGCCGCUUCCGAGACGAGGGAAUUCUACUUUUCCCGCACGAUAAGGCGCCGACGUCACUUAUUCUGCGGAUCCCGAUACAGACACCGGAGUGGGGGAGGUGUGUCUGAAGAACCCAUUCUUCCGCAAAUUCUGCUGGAAGAAAUUCUGGAGAGAGGUCUUCAGACCGCCCGAGCAUACUCCAUGCCUCCAGCGUUCCCGCAGUGUUCGCCAACUAGGGCUCUCAUGUAUGAUUGCGGGGGGUGCUCAGGCACCGCUUCCGUCCGGGGUCGCCCAGUCUCGAUCUCGGCGAGGCUUCAUAACCUAAAUUGCAGUAUUGGGCAGGGUGUUACACAAUGUUUCAUCUUAACGAAUCUUACUAACUCGCUACCUCUUCUAAGUCCUCUGGCAUUCUUUCUCCUGCACAAAUCAUAUCGUAUAUGGCUACCCUCGAGAUACCCCAAUGCACUCUUUUCCUACGCGUGUAUGCGUACGCAGGAGACAGCUCCUAUCUCUUCGACAUCGUGCUUGUCGACGCUGCAGAAACCGCUAAUACGCCGUGGGUUCUCUUACGUAACGCGAACCGUUAAGAGACCUGAGAUUUAUUUAUCUCGGGCGGUUGGAAGCUACGUGCCAUUAUCCGGCGGGGCCAACCACAAUCAAGGAGUGCCUGCUAGAGACACUCUAAGUAUUCGCCCAGCGAGCUAUAGGUCACUCCCCGACACCCGAAGGCCAGCGGGAUACAAAAGCCGCAUUACCCCUCACGACCGGCGCUGGGGACCGAAAAUACAUUUAUUCAGGGGCACGACCCCUUCCUGGCCGCAUUGGGUAGCGAAGUGCCGGUUUACGUUUAAAACUUGUAUAUGCCAGUAUGAUUUUCCAGACGGCCCAAGACACAGAUUCGCCGGCGUGAGGUCGCAGUACAGGGGCCGGAAGAAUCGCACUUUCGCUAACCAGAUAAGUAGUGUCGGGGACUUUCAAAAACCUGCUUCGAUCACCACGGGUUCGUCCCGAAAAGUAGGAGCUCGGACCUGCUCUCCUAGUGGAAUGAAACAACGACGCGUUCGGACCUAUGUUAGCUGUGGCACUGUUCACUACGCCCUGGGUCGGUCGCCCCGUCCUGUAAUAACUCUUCGGCCAUGGCGAGUUUUGACGAGCGUGUCCUUACGGGAACCAGAGGUGGAGCCACUUCCUUUUAACAGGUACCCUAUUCAACGAGGACCAUCCACUGCUACCAUCUACCAUUUACUCUCUUUUUCUAGUUUGCUAAGGUGUAUUUCCGGGGAAUCCCCGGAUAUUAGGCUCGUUGGAUCCUCAUCAUGCGACCUGACCUCGGCGGGACGGCAUCGGUGUAGGUACAGCCGGCGUUUUCUUCGCAACUGUUAUUGUAUGGAGCUCUGGAUGUUUGCAAUUCGCAAUCCACUAACGAUUCCCUCGUGCUCCAUGUCUAUAGUACUUAUCUUGAGGAUCUUUGUCGUAUGGUGCCAGACGGGGCGCCGCGCGGCUCCCACUGGUGUGCCGGUGCUACUUUACACAGUGACAGAUGCAAGCACAAUUGUUUCUCCGCCCUCGUCGAGACGACCAUGCAUGCAGACAGUUCUCAAAAUGGAUUAUCCUCAAGUCAUAGUCGGAUUACCGGCGAGGACAAGCGUUUACUUCAGGUACUUCCACGUAUGCUUUAAAUCGAAACAUGUAAUUCUAAAAAAUCCUGGACCGAUUCCAACUGAGGGAAGCGCGACUCGGAGUAGAUAUUAUGCACUGAACCUCCGAGCAGACCUUGAAUCUGUGGCCCGGCUACAUCGUGGUGGUAGGAGAUGCCUGAACAUCAGCGGGCUUAACAUACAGGCGUCUGAGAAGAAGUCGCUGGGCCCGACCCCAUAUGGCGUGCCCCUAUGUGUCACAAGCUGUGUCAGACAUAGGAUGUCUUUGACGCUUGCGACAUCGUCCGCUUUCUUAUGUAAGCAAAGUUCGGCAAUAAUUGCCUUGAUCUUUGACUUGGAUGAACCCAAAGCUAUGAAUAGAGACAGUUACGGCUCAAAAAAAAGAGGUUCACUUUUUGGGGGCCCGCUCCUGCUUGCCAUACAAUACCGGUACUCAUGCCAUGACAGGCAAACCAGAGACACAACCUCUGUGACGCUGACUCAUAAGGGCGGAGGACGACGCCACAGUCACAUCGCUAUGCCACCUGGGCCGUUAGCCUCAAGAUUGGCGAUGCAUUGCUUCCGUGUAACAACGCACACGGGAGUGCGAUUCUUCGCCCGAGCUGGCUCACGUCGCGCGCAAUGUCGGCUAGGACCGGGCAAUCUAGCUCCCGGGUUGCUUGGGCGUCACAGAUCGCAUUUGAAAGUACUCCGAGCAACCGUAUUCUUUUAUGUGUUGAUAUCGGUCAGCACGGCGUCAAACGGGUGCGCUUUAUUACAUGCAAAUUCCCGCCACGGGGCGUGUGACACCAGGACACGUCAUCGCUUGCCAGUUUAUGGGAAACUAAUAAGUGCUUGGCGAUGGACCCGGCAAAAUGCAGAACGAGUAGUGCUUAACGUCGGAUGGUUCUCGUCCCUAAGGAGAGUGACUCAGGCUACCAGGACCUCCGGGCAUAGCACUGUACAGCCGCAUCCGAAUCGGCUUCAACGAACAUUCAGGCCAAAGCAAGAGGCAAUGGGUACCCACCUUAAAAAGGGUGCGCAAUGGCGAAGACAAUGGAGGUGGUAUUUCGCUCGGGUGAUUUACCGAUGUCAACUCGUGUUUCUUGAGGGCUCCGCUGCGCCCCCCCAGCUGAGGUCCGGGCAAAUGGUUGCUGCGACGGCUUUGUUCCCUCUGAAGUGCGGCCUCCCUCCCGCUGAUGGGGGGUUUACCCUUAUGUGUGCCUUCUGCCUCCAUGGCUUAGCCAGCAGUCAUAGCAACCGCAUACAACUUGCUCCUUUCAUCUCGCCACCCUCUCAUCCGAUGCAUCGCGUAUUAUUCAUCUAUAUAGCGCGCAGUCCAGGUCACACCCGCCUGCCGGGUAUAUGGGAAUCUCUCCGGCUUGUCCACACGGCAUCUUGGUCGUCACCGACUCUUCGGUGUCACAUCCGCUUUGGCCUUAUACCUUCGGCGGAUAUAUGCCAGGAAAUAUCGACUCUGAUCACAGCUUCCUUGACUGGUCAACGCCCGCGAUUUAAAAAAAACGUACCCCAGUACUUGGGGAUUACGAAGCUGUUCAACCAGGCUCCGGAUCGGACGAGGCCUUUUGUGGUGUUUCUUAAGGAACCGGCCGACUCCCCAUCCUUUGCUGAAACGAAGUUCGAUUCAUGCCAUUAUAUGGUUCAAUUCCAAACUAAACAACAGACCGCGCUAAUGGAGGAGGAAACCCCCUCAAGGUCUGGAUUAGCCCAUCCUGAGGACAUGCAACGUCGCCUCUAUCCUUCCAAGGGGUGUCACACGCUCGAGUCAUUAUCUGUUAACGGGUGCACCGGUCUGCUCUGGUCUACCGUGACACUUCUGAGCGAUUCUUACUGGUGUUUCCUCAGUCGGGCACCCCGGAGGUUAGGGCUCGACAACAGUUCUGAUUUACCGUGUGUUCUGACGCAGGGCGCCCGAAAAAACACUCGUUGCAGCGUAUCGCAUUCAAGAAACUCUAAUGAAUCAACUACUGUCACUAAAUUACUGGCCAAGAGUGUCUUCAGUUGCAAAGCUCUCAUGCAGAUGAGAAUCUCGCUCCGUACUUCCUGGUCUAUGGGGAGUCUUGCACCUGAGCCGCAGAUGGUUUACUGGUACAAAGUAGCUAGAAUACGUCCGACGCGAUCCGAUGGUCCGGGGCCCGUAUACGUCGGAAAGUCUACAAACCGACUCCAGAAUUCUAAAAGCGUGUCCGCCUGUUCUUGUAGUGCAGCCAUGGCUACAAGUUUUGCUGCAGCUCAAGGCAAUUUCAAUUAUCUAGCCCCUCCCAACCUUGUUCACAAAAUUCCAUCUGCGCCCGGUUCUCGACCACAACUUCUCGAAACUGUAGAUAUCCCAUCCGCGUAUAAUCCGAAUAUGUGGGAGUUCGUUUUUUUUUACUCAUUUGAACGGUUCAUCGAUUCCGUUUUAUGCUCAACCCAAGAACAGGACUCCCCCCUUAACCAAACUACAGUGAGUCUUCUCCGUGAUAUAGGCGGUCAAAGCUCAGGGCAACCCUGCCUGUUGAUAUUCCUACGUAGAUUCUGGUCGCUGUGUCCCUCUCUUAUACAGGAGUCGCGCAAGAGCGCCCGUUGCUGCAGGUGCGAAGUAAAGAUAGGGUCCCAUUCGCGAACGUGUGGUGGGCGGGUAAUUCUUUUUUUACGUAGGUGGCGCAGUUCGCGACCAUCUGAUAGAAGUAGACCUGAUGUACCAAAUUAUACACGUUCAUCGUAUAAUUGUGAAGUGGAGCUGGUCGAUAACGGAUCCAUCCCCAACUGUCCUGUAACAUGGCAAAGAGCCAAAUUGAGAGUGGAUGCGCCAUGGAUAACACGCUGGCGGCCCGACGUCUGUCUCGGACAGACUGCAAGGUGGUCUUGUAUGUUGAUGCCUAACUUGUGCCAGCCUUUAUUCCAGAUUCGACUCUACCGGGGUUCCGUCUCUACCAUCACAGGGAGGUCCUUGACUCACAUAUAUGGAUCAUGGACUUCUUCCCAUUCACCAACACACAGAGGACGUGAACGGGACCCCCUUUCAGCCGCAAAGCGUGGCCGCUGCGCGCUCCGACAUCUGCCCGAUUGCGUCUUGGUAAACGUUUUGGAGGCGCGCACGACGAGCGCGGCUUAUCCUACCCCAACAAAGAUCACGCUGGUAAGGACGAUCAAUACUAAGGGAGAACAAGAGAAGUCGGCGCUACAGAACUGCCAGUUACAGUACCUAUAUAUCGACCAACGCGGCUUACAGAGUCCACUCCGUUUAACACUAUUAAACAUCUGUCACUGGGGCCCCCGAUACAUUUCGUGUUGUUACAAUCCACCAGACGAAAGCCGGUCUUACGUGGGCCGCGGGGGGGCCAGGCGGCACGGAGUAGUACACUUAAACAAAAAGCACCCGUGGGCAGUAAAGGAAGGUCGUAAGCUUAGUCAAGCCAGAUGGAUUAUAUCCGAGUGCAGGUGCCUUUAUCAACGGGGAACAGCAGUGGAUACUUACAAACGAGUAGGGAAGCUAUUUACAAGGACGGAUCUCUUCGGCUCGAUCGAAACGUCGACCGGUAAGACGCCAUUAAACACGUGGUAUGCCACGUCAGAGCAGCAAACAACCUCCGUAUGCUUCUACCAUGCAUUGCGAGAAACUUCGAGGAGCCGAAUCACCCCUCGGGUCUCGUUCUUAUAUUUGCUAUGCGUGAUUAGACUCGUCUCCAUGGAUAAGGGCAGCUUGCACCGCGUACUUAACUUUGAUGGUUUUGGAUUCCUCAAUAGUUGUAGGGCUUCCGCAAAAAGUACAGUUGCGACGGCAAUGUUCGCCAGAGUAACUCGGGGUACAUACCGUGCUAGUGCAUCACGGCGGCAACCCACCGUGGAUCGCCAGCGCGACGUUCCCAUGAAGCGAGGUCACCUAUUUGGACGCCCGUGCCGAGUAACGUGCAGUUGUGCCGUAAGCCUGGGCGAAUCGACUGGCCAAAAGGCUACAGUACUCCUUUCCCAGAUGCUGGCUCGUCAAGGUGAGCUGGGGCGCUCGACACGUAAAGUGUCCAAUUCGGUGUCCUCUUCCACACUCUGGGGGCUGUUUGCAAGUAUAGGCGGGAGGGGUCUCAUCGACCUGUCAAAUAACGCGAAGACGCUUCCCAGGGAACAUAAGAGGGGCGUCCCGGUAGUACCUGGUAAGGCGGGUCGAAACAGAUUGGACCUUGUACACUCAGAUUACCCUUCUGAUUGGGCCGGCUGCGUACACUCGGACAUUUCCAUCCUAAGUAGAUGCCGUCAUUCCGUCCCUUCGAUGUGGAGAAGGUUGAUCCUCGCCAGGGCAUGUAACAAAAUACCCAUACUGGAUUACGCGCGUAUCGUGAGGUGGACAGCUCGCAUAUACACUGUACUGCUACAGAAUCUCUUCCAGUUAGAACGCCUUCACUCCGGCAAGCGAGCUGAACCUUUCGAUUCAAGAUUAUAUCCCCCCGCGCGGGUAAAUUCAGAGGACCGUGGGCCACUAUCACUCAGCUUGGCGCUCCAGUCCUCAAACACCCUCGCCACUGAGGAAGAGGGUCGACUGAUUGCUGGAUAUGCUGACCACAUGUCGCUAUCUACAAAAUGCGUUACGAACUUCCGAUACGCUGCUCUGCAUAAAUGUGCUUCCGUGGUUUGGCGUUGGUCGCACAAUGAUAGUAGGCUGCCUGAAAGCUCAUCAUUUCCCGAUGAGUGGACUGGCGCCAUUUCCCUACCAUCUUCGUUGAUGCAGGUGAAGACCCACUAUCACGCUUACAAGAACAAUAGGUAUCCCAGCCCCUCUGAUUCCGGGCCAGACUGCGUCGCCUAUACAAGAUCGCAGGUUUUACUACACUGGUUUGCUGGUGAUGUCGUGCGCGACCCGGCACCACACCUUAAGACAAAAUUACUACGCGGUUCGCAGAAGAUCUCUUGGCUCGUAGGGAAGGUCCGGAAUAUAUGGAAGCCCAUUGCGCGAAUUGUUGACUGUCCGCGGCCCGAUCCAUAUGAGGGUGCUGUGCUCGUGGAGGUAUAA'
    print(translate(rna))

