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

def orf_finder(dna_seq):
    orf_seq = ""
    positive_starts = start_codon_finder(dna_seq)
    positive_stops = stop_codon_finder(dna_seq)
    negative_starts = start_codon_finder(reverse_complement(dna_seq))
    negative_stops = stop_codon_finder(reverse_complement(dna_seq))
    if max(positive_stops) - min(positive_starts) > max(negative_stops) - min(negative_starts):
        orf_seq +=

    return orf_seq

print(find_start_codons("ATGCATGCGATGTAGACGTAGCTGACGATG"))
print(find_stop_codons("ATGCATGCGATGTAGACGTAGCTGACGATG"))
print(find_start_codons(reverse_complement("ATGCATGCGATGTAGACGTAGCTGACGATG")))
print(find_stop_codons(reverse_complement("ATGCATGCGATGTAGACGTAGCTGACGATG")))

