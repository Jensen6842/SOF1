ATOMS = {
    'H': {'name': 'Hydrogen', 'weight': 1.00797},
    'He': {'name': 'Helium', 'weight': 4.00260},
    'C': {'name': 'Carbon', 'weight': 12.011},
    'N': {'name': 'Nitrogen', 'weight': 14.0067},
    'O': {'name': 'Oxygen', 'weight': 15.9994},
    'Ca': {'name': 'Calium', 'weight': 40.08}
    }


def molar_mass(molecule):
    mass = 0
    for i in range(len(molecule)):
        if molecule[i][0] not in ATOMS:
            raise ValueError
        else:
            mass += ATOMS[molecule[i][0]]['weight'] * molecule[i][1]
    return mass
