from utils import get_monoisotopic_mass_table


def solve():
    table = get_monoisotopic_mass_table()
    f = open('./spec/input.txt', 'r')
    lines = f.readlines()
    f.close()
    masses = list(map(lambda x: float(x.strip()), lines))
    final_residue = ''
    for i in range(len(masses) - 1):
        final_residue += get_amino_acid(masses[i], masses[i + 1])
    print(final_residue)

def get_amino_acid(mass1: float, mass2: float) -> str:
    mass_diff = abs(mass1 - mass2)
    table = get_monoisotopic_mass_table()
    for aa, mass in table.items():
        if abs(mass_diff - mass) < 0.01:
            return aa
    raise ValueError('not found')

