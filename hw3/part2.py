def translate(sequence):
    amino_acids = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
        'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W'
    }
    codons = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        if len(codon) == 3:
            codons.append(codon)
    aa_seq = ""
    for bases in codons:
        aa_seq += amino_acids[bases]
    return aa_seq


my_dict = {}
dna_seq = ""

with open("Hw03_CDS_seqs.txt") as infh:
    for line in infh:
        if line.startswith(">"):
            gene_name = line.split()[0][1:]
            continue
        elif line == "\n":
            my_dict[gene_name] = {"name": gene_name, "DNA_sequence": dna_seq, "DNA_sequence_length": len(dna_seq),
                                  "Protein_sequence": translate(dna_seq), "Protein_length": len(translate(dna_seq))}
            dna_seq = ""
            continue
        else:
            dna_seq += line.strip()
    my_dict[gene_name] = {"name": gene_name, "DNA_sequence": dna_seq, "DNA_sequence_length": len(dna_seq),
                          "Protein_sequence": translate(dna_seq), "Protein_length": len(translate(dna_seq))}
