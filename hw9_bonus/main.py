class Protein:
    def __init__(self, proteinName):
        self.proteinName = proteinName
        self.listOfResidues = {}


class Residue:
    def __init__(self, residue_name, residue_number):
        self.residue_name = residue_name
        self.residue_number = residue_number
        self.listOfAtoms = {}

    def add_atom(self, atom):
        self.listOfAtoms[atom.atom_number] = atom


class Atom:
    def __init__(self, atom_name, element_type, atom_number, xyz_crd):
        self.atom_name = atom_name
        self.element_type = element_type
        self.atom_number = atom_number
        self.xyz_crd = tuple(map(float, xyz_crd))


def pdbread(file_name):
    compnd_counter = 0
    with open(file_name) as infh:
        protein = Protein(None)
        residue = None

        for line in infh:
            if line.startswith('COMPND') and protein.proteinName is None:
                compnd_counter += 1
                if compnd_counter == 2:
                    protein.proteinName = line.strip("\n").split()[3][:-1]
            elif line.startswith("ATOM"):
                atom1, atom_number, atom_name, residue_name, chain, residue_id, x, y, z, occupancy, c_factor, element = line.strip("\n").split()
                if residue is None or residue.residue_number != residue_id:
                    residue = Residue(residue_name, residue_id)
                    protein.listOfResidues[residue_id] = residue

                atom = Atom(atom_name, element, atom_number, (x, y, z))
                residue.listOfAtoms[atom_number] = atom
    return protein


my_protein = pdbread("1UBQ.pdb")
print(my_protein)
print(my_protein.proteinName)  # UBIQUITIN
print(list(my_protein.listOfResidues.keys()))  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', ... '76']
print(my_protein.listOfResidues["2"].residue_name)  # GLN
print(list(my_protein.listOfResidues["2"].listOfAtoms.keys()))  # ['10', '11', '12', '13', '14', '15', '16', '17']
print(my_protein.listOfResidues["2"].listOfAtoms["12"].xyz_crd)  # [24.865, 29.024, 5.33]
