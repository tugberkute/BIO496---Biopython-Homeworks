def DNA_validation(dna_seq: str):
    """
    :param dna_seq: A string of DNA sequence
    :return: True if it is valid, False if it is not.
    """
    dna_seq = dna_seq.upper()
    valid_bases = ["A", "T", "G", "C"]
    valid = True
    for base in dna_seq:
        if base not in valid_bases:
            valid = False
    return valid


def start_codon_finder(dna_seq):
    start_codons = []
    for i in range(len(dna_seq) - 2):
        codon = dna_seq[i:i+3]
        if codon == "ATG":
            start_codons.append(i)
    return start_codons


def stop_codon_finder(dna_seq):
    stop_codons = []
    for i in range(len(dna_seq) - 2):
        codon = dna_seq[i:i+3]
        if codon in ["TAA", "TGA", "TAG"]:
            stop_codons.append(i)
    return stop_codons


def orf_finder(dna_seq):
    orf_seq = ""
    positive_starts = start_codon_finder(dna_seq)
    positive_stops = stop_codon_finder(dna_seq)
    negative_starts = start_codon_finder(reverse_complement(dna_seq))
    negative_stops = stop_codon_finder(reverse_complement(dna_seq))
    if max(positive_stops) - min(positive_starts) > max(negative_stops) - min(negative_starts):
        orf_seq += dna_seq[min(positive_starts):(max(positive_stops) + 3)]
    elif max(positive_stops) - min(positive_starts) < max(negative_stops) - min(negative_starts):
        orf_seq += dna_seq[min(negative_starts):(max(negative_stops) + 3)]
    return orf_seq


def complement(dna_seq):
    """
    Calculates the complementary base according to DNA sequence that is taken from the user. It gives the complement as
    a capitalized string.

    :param dna_seq: A DNA sequence from user.
    :return: Complement of the sequence
    """
    capital_seq = dna_seq.upper()
    complement = ""
    for base in capital_seq:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement


def reverse(dna_seq):
    """
    Reverses the DNA sequence that is taken from the user. It gives the reverse as a capitalized string.

    :param dna_seq: A DNA sequence from user.
    :return: Reverse of the sequence
    """
    capital_seq = dna_seq.upper()
    reverse = ""

    for base in range(-1, -len(capital_seq) - 1, -1):
        reverse += capital_seq[base]
    return reverse


def reverse_complement(dna_seq):
    """
    Calculates the complement of the reversed DNA sequence that is taken from the user. This function first calculates
    the reverse of the sequence, then takes its complement by using previous two functions. It gives the
    reverse-complement as a capitalized string.

    :param dna_seq: A DNA sequence from user.
    :return:Reverse-complement of the sequence
    """
    return complement(reverse(dna_seq))


def translate(orf):
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
    orf_codons = []
    for i in range(0, len(orf), 3):
        codon = orf[i:i + 3]
        orf_codons.append(codon)
    aa_seq = ""
    for bases in orf_codons:
        aa_seq += amino_acids[bases]
    return aa_seq


def main():
    give_until_valid = True
    while give_until_valid:
        user_input = input("Please give a DNA sequence: ")
        if DNA_validation(user_input):
            if len(user_input) >= 300:
                print(translate(orf_finder(user_input)))
                give_until_valid = False
                continue
            else:
                print("Please give a DNA sequence longer than 300 bases!")
        else:
            print("DNA sequence is not valid!")


main()
